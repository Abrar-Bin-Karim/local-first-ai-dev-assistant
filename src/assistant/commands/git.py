"""Git history reasoning commands."""

import typer
from pathlib import Path
from rich.table import Table
from rich.console import Console
from assistant.utils.ui import show_header, show_info, show_error, show_warning

console = Console()
app = typer.Typer()

@app.command()
def history(limit: int = 10, author: str = None):
    """
    Show git commit history.
    
    Examples:
        assistant git history
        assistant git history --limit 20
        assistant git history --author "John"
    """
    import subprocess
    
    # Check if git repository exists
    result = subprocess.run(["git", "rev-parse", "--git-dir"], capture_output=True, text=True)
    if result.returncode != 0:
        show_error("Not a git repository")
        return
    
    show_header(f"Git History (last {limit} commits)")
    
    # Build git log command
    cmd = ["git", "log", f"--max-count={limit}", "--pretty=format:%h|%an|%ad|%s", "--date=short"]
    
    if author:
        cmd.append(f"--author={author}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        show_error("Failed to get git history")
        return
    
    commits = result.stdout.strip().split('\n') if result.stdout else []
    
    if not commits:
        show_warning("No commits found")
        return
    
    # Display commits as table
    table = Table(title="Commit History")
    table.add_column("Hash", style="cyan", no_wrap=True)
    table.add_column("Author", style="green")
    table.add_column("Date", style="yellow")
    table.add_column("Message", style="white")
    
    for commit in commits:
        if '|' not in commit:
            continue
        parts = commit.split('|', 3)
        if len(parts) == 4:
            table.add_row(parts[0], parts[1], parts[2], parts[3])
    
    console.print(table)

@app.command()
def blame(file: str, lines: int = 10):
    """
    Show who last modified each line.
    
    Example:
        assistant git blame src/assistant/cli.py
    """
    import subprocess
    
    file_path = Path(file)
    if not file_path.exists():
        show_error(f"File not found: {file}")
        return
    
    show_header(f"Git Blame: {file}")
    
    result = subprocess.run(["git", "blame", "--date=short", file], capture_output=True, text=True)
    
    if result.returncode != 0:
        show_error("Failed to get blame information")
        return
    
    blame_lines = result.stdout.strip().split('\n')[:lines]
    
    for line in blame_lines:
        if '(' in line:
            author_part = line.split('(')[1].split(')')[0]
            console.print(f"[dim]{author_part[:30]}[/dim] → {line.split(')')[-1][:80]}")

@app.command()
def changed(between: str = None):
    """
    Show what changed between commits.
    
    Examples:
        assistant git changed
        assistant git changed --between "HEAD~5..HEAD"
    """
    import subprocess
    
    range_spec = between or "HEAD~5..HEAD"
    show_header(f"Changes: {range_spec}")
    
    result = subprocess.run(["git", "diff", "--stat", range_spec], capture_output=True, text=True)
    
    if result.stdout:
        console.print(result.stdout)
    else:
        show_info("No changes found")