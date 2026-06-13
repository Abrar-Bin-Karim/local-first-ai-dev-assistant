"""Configuration management commands."""

import typer
from pathlib import Path
from rich.table import Table
from assistant.utils.ui import show_header, show_success, show_error, show_info, console

app = typer.Typer()
_config = {}  # Placeholder - will use utils.config later

@app.command()
def show():
    """Show current configuration."""
    show_header("Current Configuration")
    console.print("[yellow]Config system coming soon![/yellow]")
    console.print("Run: assistant config init to get started")

@app.command()
def init():
    """Initialize configuration."""
    show_success("Config initialized")