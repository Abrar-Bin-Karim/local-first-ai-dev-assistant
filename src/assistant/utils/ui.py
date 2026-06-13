"""Rich UI components for consistent output."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

def show_info(message: str):
    """Show info message."""
    console.print(f"[blue]ℹ[/blue] {message}")

def show_success(message: str):
    """Show success message."""
    console.print(f"[green]✓[/green] {message}")

def show_warning(message: str):
    """Show warning message."""
    console.print(f"[yellow]⚠[/yellow] {message}")

def show_error(message: str):
    """Show error message."""
    console.print(f"[red]✗[/red] {message}")

def show_header(title: str):
    """Show section header."""
    console.print(Panel(title, box=box.ROUNDED, style="cyan"))

def show_table(columns: list, rows: list, title: str = None):
    """Show a formatted table."""
    table = Table(title=title, box=box.SIMPLE)
    for col in columns:
        table.add_column(col)
    for row in rows:
        table.add_row(*[str(cell) for cell in row])
    console.print(table)