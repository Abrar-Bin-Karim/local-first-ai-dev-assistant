"""Repository understanding commands."""

import typer
from pathlib import Path
from rich.console import Console
from rich.tree import Tree
from rich.table import Table
from assistant.utils.ui import show_header, show_info, show_error, show_success, show_warning
from assistant.utils.ignore import IgnoreRules

console = Console()
app = typer.Typer()


@app.command()
def explain(path: str = "."):
    """
    Explain repository structure.
    
    Example:
        assistant repo explain .
        assistant repo explain src/
    """
    target_path = Path(path)
    
    if not target_path.exists():
        show_error(f"Path does not exist: {path}")
        raise typer.Exit(1)
    
    show_header(f"Repository: {target_path.absolute()}")
    
    # Determine repo root (use target path if directory, otherwise its parent)
    repo_root = target_path if target_path.is_dir() else target_path.parent
    ignore_rules = IgnoreRules(repo_root)
    
    # Count files by extension
    extensions = {}
    total_files = 0
    ignored_files = 0
    
    # Walk through directory
    if target_path.is_dir():
        search_path = target_path
    else:
        search_path = target_path.parent
    
    for file in search_path.rglob("*"):
        if file.is_file():
            if ignore_rules.is_ignored(file):
                ignored_files += 1
                continue
            
            total_files += 1
            ext = file.suffix or "no extension"
            extensions[ext] = extensions.get(ext, 0) + 1
    
    # Show statistics
    table = Table(title="Repository Statistics")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Total files", str(total_files))
    table.add_row("Ignored files", str(ignored_files))
    table.add_row("File types", str(len(extensions)))
    table.add_row("Repository root", str(repo_root.absolute()))
    console.print(table)
    
    # Show top extensions
    if extensions:
        show_info("Top file types:")
        sorted_ext = sorted(extensions.items(), key=lambda x: x[1], reverse=True)[:5]
        for ext, count in sorted_ext:
            # Show percentage
            percentage = (count / total_files) * 100 if total_files > 0 else 0
            console.print(f"  {ext}: {count} files ({percentage:.1f}%)")


@app.command()
def tree(path: str = ".", depth: int = 2):
    """
    Show directory tree structure.
    
    Example:
        assistant repo tree
        assistant repo tree src/ --depth 3
    """
    target_path = Path(path)
    
    if not target_path.exists():
        show_error(f"Path does not exist: {path}")
        raise typer.Exit(1)
    
    # Determine repo root for ignore rules
    repo_root = target_path if target_path.is_dir() else target_path.parent
    ignore_rules = IgnoreRules(repo_root)
    
    def add_tree_nodes(directory: Path, tree_root: Tree, current_depth: int):
        if current_depth > depth:
            return
        
        try:
            items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        except PermissionError:
            return
        
        for item in items:
            # Skip ignored items
            if ignore_rules.is_ignored(item):
                continue
            
            if item.is_dir():
                branch = tree_root.add(f"[bold cyan]📁 {item.name}[/bold cyan]")
                add_tree_nodes(item, branch, current_depth + 1)
            else:
                # Show file size for files
                try:
                    size = item.stat().st_size
                    if size < 1024:
                        size_str = f"{size}B"
                    elif size < 1024 * 1024:
                        size_str = f"{size / 1024:.1f}KB"
                    else:
                        size_str = f"{size / (1024 * 1024):.1f}MB"
                    tree_root.add(f"[dim]📄 {item.name}[/dim] [grey54]({size_str})[/grey54]")
                except:
                    tree_root.add(f"[dim]📄 {item.name}[/dim]")
    
    show_header(f"Directory Tree: {target_path}")
    console.print(f"[dim]Depth limit: {depth} levels[/dim]\n")
    main_tree = Tree(f"[bold]📂 {target_path.name}[/bold]")
    add_tree_nodes(target_path, main_tree, 0)
    console.print(main_tree)


@app.command()
def files(pattern: str = "*", show_ignored: bool = False):
    """
    List files matching pattern.
    
    Examples:
        assistant repo files "*.py"
        assistant repo files "test_*.py"
        assistant repo files "*.md" --show-ignored
    """
    from pathlib import Path
    
    repo_root = Path(".").resolve()
    ignore_rules = IgnoreRules(repo_root)
    
    matches = list(repo_root.rglob(pattern))
    
    filtered_matches = []
    ignored_matches = []
    
    for m in matches:
        if m.is_file():
            if ignore_rules.is_ignored(m):
                ignored_matches.append(m)
            else:
                filtered_matches.append(m)
    
    # Display results
    show_header(f"Files matching: {pattern}")
    
    if filtered_matches:
        show_success(f"Found {len(filtered_matches)} file(s)")
        for m in filtered_matches[:20]:  # Limit to 20
            # Show relative path
            rel_path = m.relative_to(repo_root)
            # Show file size
            size = m.stat().st_size
            if size < 1024:
                size_str = f"{size}B"
            elif size < 1024 * 1024:
                size_str = f"{size / 1024:.1f}KB"
            else:
                size_str = f"{size / (1024 * 1024):.1f}MB"
            console.print(f"  📄 {rel_path} [dim]({size_str})[/dim]")
        
        if len(filtered_matches) > 20:
            console.print(f"  ... and {len(filtered_matches) - 20} more")
    else:
        show_warning(f"No files found matching: {pattern}")
    
    # Show ignored files if requested
    if show_ignored and ignored_matches:
        console.print(f"\n[yellow]Ignored files ({len(ignored_matches)}):[/yellow]")
        for m in ignored_matches[:10]:
            rel_path = m.relative_to(repo_root)
            console.print(f"  [dim]🚫 {rel_path}[/dim]")
        if len(ignored_matches) > 10:
            console.print(f"  ... and {len(ignored_matches) - 10} more")


@app.command()
def stats(path: str = "."):
    """
    Show detailed statistics about the repository.
    
    Example:
        assistant repo stats
    """
    target_path = Path(path)
    
    if not target_path.exists():
        show_error(f"Path does not exist: {path}")
        raise typer.Exit(1)
    
    show_header(f"Repository Statistics: {target_path}")
    
    repo_root = target_path if target_path.is_dir() else target_path.parent
    ignore_rules = IgnoreRules(repo_root)
    
    # Detailed statistics
    extensions = {}
    file_sizes = []
    largest_files = []
    total_size = 0
    total_files = 0
    
    search_path = target_path if target_path.is_dir() else target_path.parent
    
    for file in search_path.rglob("*"):
        if file.is_file() and not ignore_rules.is_ignored(file):
            total_files += 1
            size = file.stat().st_size
            total_size += size
            file_sizes.append(size)
            
            ext = file.suffix or "no extension"
            extensions[ext] = extensions.get(ext, 0) + 1
            
            # Track largest files
            largest_files.append((file, size))
    
    # Sort largest files
    largest_files.sort(key=lambda x: x[1], reverse=True)
    
    # Calculate average file size
    avg_size = total_size / total_files if total_files > 0 else 0
    
    # Size distribution
    tiny = sum(1 for s in file_sizes if s < 1024)  # < 1KB
    small = sum(1 for s in file_sizes if 1024 <= s < 10240)  # 1KB - 10KB
    medium = sum(1 for s in file_sizes if 10240 <= s < 102400)  # 10KB - 100KB
    large = sum(1 for s in file_sizes if 102400 <= s < 1048576)  # 100KB - 1MB
    huge = sum(1 for s in file_sizes if s >= 1048576)  # > 1MB
    
    # Display stats
    stats_table = Table(title="File Statistics")
    stats_table.add_column("Metric", style="cyan")
    stats_table.add_column("Value", style="green")
    
    stats_table.add_row("Total files", f"{total_files:,}")
    stats_table.add_row("Total size", f"{total_size / (1024 * 1024):.2f} MB")
    stats_table.add_row("Average file size", f"{avg_size / 1024:.2f} KB")
    stats_table.add_row("Largest file", f"{largest_files[0][1] / (1024 * 1024):.2f} MB" if largest_files else "N/A")
    
    console.print(stats_table)
    
    # Size distribution
    console.print("\n[bold]Size Distribution:[/bold]")
    dist_table = Table(show_header=False, box=None)
    dist_table.add_column("Size", style="cyan")
    dist_table.add_column("Count", style="green")
    dist_table.add_column("Percentage", style="yellow")
    
    def add_dist(label, count):
        pct = (count / total_files) * 100 if total_files > 0 else 0
        dist_table.add_row(label, f"{count:,}", f"{pct:.1f}%")
    
    add_dist("< 1KB", tiny)
    add_dist("1KB - 10KB", small)
    add_dist("10KB - 100KB", medium)
    add_dist("100KB - 1MB", large)
    add_dist("> 1MB", huge)
    
    console.print(dist_table)
    
    # Top extensions
    if extensions:
        console.print("\n[bold]Top 10 File Types:[/bold]")
        ext_table = Table(show_header=True)
        ext_table.add_column("Extension", style="cyan")
        ext_table.add_column("Count", style="green")
        ext_table.add_column("Percentage", style="yellow")
        
        sorted_ext = sorted(extensions.items(), key=lambda x: x[1], reverse=True)[:10]
        for ext, count in sorted_ext:
            pct = (count / total_files) * 100 if total_files > 0 else 0
            ext_table.add_row(ext, f"{count:,}", f"{pct:.1f}%")
        
        console.print(ext_table)
    
    # Top 5 largest files
    if largest_files:
        console.print("\n[bold]Top 5 Largest Files:[/bold]")
        for file, size in largest_files[:5]:
            rel_path = file.relative_to(repo_root)
            size_mb = size / (1024 * 1024)
            console.print(f"  📄 {rel_path} [dim]({size_mb:.2f} MB)[/dim]")


if __name__ == "__main__":
    app()