"""Repository understanding commands."""

import typer
from pathlib import Path
from rich.console import Console
from rich.tree import Tree
from rich.table import Table
from assistant.utils.ui import show_header, show_info, show_error, show_success

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
    
    # Count files by extension
    extensions = {}
    total_files = 0
    
    for file in target_path.rglob("*"):
        if file.is_file() and not any(x in file.parts for x in ['.venv', '__pycache__', '.git']):
            total_files += 1
            ext = file.suffix or "no extension"
            extensions[ext] = extensions.get(ext, 0) + 1
    
    # Show statistics
    table = Table(title="Repository Statistics")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Total files", str(total_files))
    table.add_row("File types", str(len(extensions)))
    table.add_row("Path", str(target_path.absolute()))
    console.print(table)
    
    # Show top extensions
    if extensions:
        show_info("Top file types:")
        sorted_ext = sorted(extensions.items(), key=lambda x: x[1], reverse=True)[:5]
        for ext, count in sorted_ext:
            console.print(f"  {ext}: {count} files")

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
    
    def add_tree_nodes(directory: Path, tree_root: Tree, current_depth: int):
        if current_depth > depth:
            return
        
        try:
            items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        except PermissionError:
            return
        
        for item in items:
            if item.name.startswith('.') or item.name in ['.venv', '__pycache__']:
                continue
            
            if item.is_dir():
                branch = tree_root.add(f"[bold cyan]📁 {item.name}[/bold cyan]")
                add_tree_nodes(item, branch, current_depth + 1)
            else:
                tree_root.add(f"[dim]📄 {item.name}[/dim]")
    
    show_header(f"Directory Tree: {target_path}")
    main_tree = Tree(f"[bold]📂 {target_path.name}[/bold]")
    add_tree_nodes(target_path, main_tree, 0)
    console.print(main_tree)

@app.command()
def files(pattern: str = "*"):
    """
    List files matching pattern.
    
    Example:
        assistant repo files "*.py"
        assistant repo files "test_*.py"
    """
    from pathlib import Path
    
    matches = list(Path(".").rglob(pattern))
    matches = [m for m in matches if '.venv' not in m.parts and '__pycache__' not in m.parts]
    
    if not matches:
        show_warning(f"No files found matching: {pattern}")
        return
    
    show_success(f"Found {len(matches)} file(s)")
    for m in matches[:20]:  # Limit to 20
        console.print(f"  📄 {m}")
    
    if len(matches) > 20:
        console.print(f"  ... and {len(matches) - 20} more")