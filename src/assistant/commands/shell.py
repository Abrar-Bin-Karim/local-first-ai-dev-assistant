"""Shell command explanation and risk detection."""

import typer
import re
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from assistant.utils.ui import show_header, show_warning, show_error, console

app = typer.Typer()

# Risky command patterns
RISKY_COMMANDS = {
    r'rm\s+-rf': "⚠️  Recursive force delete - can permanently remove files",
    r'sudo': "🔐  Requires administrator privileges",
    r'>\s*/dev/sda': "💀  Direct disk write - potentially destructive",
    r'dd\s+if=': "💀  Low-level disk operation",
    r'format\s+': "⚠️  Format command - will erase data",
    r':\(\)\s*\{\s*:\|:&\s*\};:': "💀  Fork bomb - will crash system",
    r'chmod\s+777': "⚠️  Overly permissive - security risk",
    r'curl.*\|\s*bash': "⚠️  Downloading and executing remote code",
    r'wget.*\|\s*bash': "⚠️  Downloading and executing remote code",
    r'kill\s+-9': "⚠️  Force kill process - may cause data loss",
    r'>\s*/etc/': "💀  Modifying system configuration",
}

@app.command()
def explain(command: str):
    """
    Explain a shell command and flag risks.
    
    Examples:
        assistant shell explain "rm -rf temp/"
        assistant shell explain "sudo apt update"
    """
    show_header("Shell Command Analysis")
    
    # Display original command
    console.print(Panel(command, title="[bold]Command[/bold]", style="cyan"))
    
    # Detect risks
    risks_found = []
    for pattern, risk_msg in RISKY_COMMANDS.items():
        if re.search(pattern, command, re.IGNORECASE):
            risks_found.append(risk_msg)
    
    # Show risk assessment
    if risks_found:
        console.print("\n[bold red]⚠️  Security Risks Detected:[/bold red]")
        for risk in risks_found:
            console.print(f"  {risk}")
    else:
        console.print("\n[bold green]✓ No immediate security risks detected[/bold green]")
    
    # Basic command parsing
    parts = command.split()
    if parts:
        console.print(f"\n[bold]Command:[/bold] {parts[0]}")
        if len(parts) > 1:
            console.print(f"[bold]Arguments:[/bold] {' '.join(parts[1:])}")
    
    # Suggest safe alternatives for risky commands
    if 'rm -rf' in command and '/' in command:
        console.print("\n[bold yellow]💡 Safer alternative:[/bold yellow]")
        console.print("  • Move to trash instead: `trash-put <file>`")
        console.print("  • Use interactive mode: `rm -ri <directory>`")

@app.command()
def safe(command: str):
    """
    Check if a command is safe to run.
    
    Example:
        assistant shell safe "rm -rf /tmp/test"
    """
    explain(command)  # Reuse the same logic
    
    # Return exit code 1 if risky
    for pattern in RISKY_COMMANDS:
        if re.search(pattern, command, re.IGNORECASE):
            raise typer.Exit(1)
    raise typer.Exit(0)