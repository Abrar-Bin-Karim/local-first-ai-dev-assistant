"""Configuration management commands."""

import typer
from pathlib import Path
from rich.table import Table
from assistant.utils.ui import show_header, show_success, show_error, show_info, console
from assistant.utils.config import Config, CONFIG_PATH, create_default_config

app = typer.Typer()
config = Config()

@app.command()
def show():
    """Show current configuration."""
    show_header("Current Configuration")
    data = config.show()
    if not data:
        show_info("No configuration file found. Run `assistant config init` to create one.")
        return
    table = Table(title="Settings")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")
    for key, value in data.items():
        table.add_row(str(key), str(value))
    console.print(table)

@app.command()
def init():
    """Initialize configuration file with defaults."""
    if config.config_file.exists():
        show_info(f"Config already exists at {config.config_file}")
        return
    config.save()
    show_success(f"Config initialized at {config.config_file}")

@app.command()
def set(key: str, value: str):
    """Set a configuration value."""
    # Try to convert to appropriate type
    if value.lower() == "true":
        value = True
    elif value.lower() == "false":
        value = False
    elif value.isdigit():
        value = int(value)
    elif value.replace('.', '', 1).isdigit():
        value = float(value)
    config.set(key, value)
    show_success(f"{key} = {value}")

@app.command()
def get(key: str):
    """Get a configuration value."""
    value = config.get(key)
    if value is None:
        show_error(f"Key '{key}' not found")
        raise typer.Exit(1)
    console.print(f"{key} = {value}")

    