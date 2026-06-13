"""Log analysis commands."""

import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from collections import Counter
from assistant.utils.ui import show_header, show_info, show_error, show_warning, show_success

console = Console()
app = typer.Typer()

@app.command()
def analyze(file: str, lines: int = 100):
    """
    Analyze log file for errors and patterns.
    
    Examples:
        assistant logs analyze app.log
        assistant logs analyze app.log --lines 500
    """
    log_path = Path(file)
    
    if not log_path.exists():
        show_error(f"Log file not found: {file}")
        raise typer.Exit(1)
    
    show_header(f"Log Analysis: {log_path.name}")
    
    # Read log file
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            all_lines = f.readlines()
            log_lines = all_lines[-lines:] if len(all_lines) > lines else all_lines
    except Exception as e:
        show_error(f"Cannot read file: {e}")
        raise typer.Exit(1)
    
    # Analyze patterns
    error_patterns = ['error', 'exception', 'failed', 'critical']
    warning_patterns = ['warning', 'warn', 'deprecated']
    info_patterns = ['info', 'started', 'completed']
    
    errors = []
    warnings = []
    infos = []
    
    for line in log_lines:
        line_lower = line.lower()
        if any(p in line_lower for p in error_patterns):
            errors.append(line.strip())
        elif any(p in line_lower for p in warning_patterns):
            warnings.append(line.strip())
        elif any(p in line_lower for p in info_patterns):
            infos.append(line.strip())
    
    # Show statistics
    stats_table = Table(title="Log Statistics")
    stats_table.add_column("Metric", style="cyan")
    stats_table.add_column("Count", style="green")
    stats_table.add_row("Total lines analyzed", str(len(log_lines)))
    stats_table.add_row("Errors found", f"[red]{len(errors)}[/red]")
    stats_table.add_row("Warnings found", f"[yellow]{len(warnings)}[/yellow]")
    stats_table.add_row("Info events", str(len(infos)))
    console.print(stats_table)
    
    # Show recent errors
    if errors:
        console.print("\n[bold red]Recent Errors:[/bold red]")
        for error in errors[-5:]:
            console.print(f"  ✗ {error[:100]}")
    
    # Show recent warnings
    if warnings:
        console.print("\n[bold yellow]Recent Warnings:[/bold yellow]")
        for warning in warnings[-3:]:
            console.print(f"  ⚠ {warning[:100]}")
    
    # Suggest actions
    if errors:
        console.print(Panel("[bold]Suggested Actions:[/bold]\n• Check error messages above\n• Review recent code changes\n• Verify configuration files", style="yellow"))

@app.command()
def watch(file: str):
    """
    Stream log file in real-time (like tail -f).
    
    Example:
        assistant logs watch app.log
    """
    import time
    from pathlib import Path
    
    log_path = Path(file)
    if not log_path.exists():
        show_error(f"Log file not found: {file}")
        raise typer.Exit(1)
    
    show_info(f"Watching {file} (Ctrl+C to stop)")
    
    try:
        with open(log_path, 'r') as f:
            # Go to end of file
            f.seek(0, 2)
            
            while True:
                line = f.readline()
                if line:
                    # Color-code based on content
                    if 'error' in line.lower() or 'exception' in line.lower():
                        console.print(f"[red]{line.rstrip()}[/red]")
                    elif 'warning' in line.lower() or 'warn' in line.lower():
                        console.print(f"[yellow]{line.rstrip()}[/yellow]")
                    else:
                        console.print(f"[dim]{line.rstrip()}[/dim]")
                else:
                    time.sleep(0.1)
    except KeyboardInterrupt:
        console.print("\n[dim]Stopped watching[/dim]")