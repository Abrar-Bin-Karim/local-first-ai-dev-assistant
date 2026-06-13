"""Token and cost management commands."""

import typer
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from assistant.utils.ui import show_header, show_info, show_warning, show_success, show_error

console = Console()
app = typer.Typer()

# Mock budget state (will connect to real engine later)
_budget_state = {
    "used": 0.0,
    "limit": 10.0,
    "tokens_used": 0,
    "tokens_limit": 1000000
}

@app.command()
def status():
    """
    Show current budget and token usage.
    
    Example:
        assistant budget status
    """
    show_header("Budget Status")
    
    # Calculate percentages
    used_percent = (_budget_state["used"] / _budget_state["limit"]) * 100 if _budget_state["limit"] > 0 else 0
    tokens_percent = (_budget_state["tokens_used"] / _budget_state["tokens_limit"]) * 100 if _budget_state["tokens_limit"] > 0 else 0
    
    # Create status table
    table = Table(title="Usage Summary")
    table.add_column("Resource", style="cyan")
    table.add_column("Used", style="yellow")
    table.add_column("Limit", style="green")
    table.add_column("Usage", style="white")
    
    # Color-code based on usage
    cost_color = "green" if used_percent < 50 else "yellow" if used_percent < 80 else "red"
    token_color = "green" if tokens_percent < 50 else "yellow" if tokens_percent < 80 else "red"
    
    table.add_row("💰 Budget", f"${_budget_state['used']:.2f}", f"${_budget_state['limit']:.2f}", f"[{cost_color}]{used_percent:.1f}%[/{cost_color}]")
    table.add_row("🎫 Tokens", f"{_budget_state['tokens_used']:,}", f"{_budget_state['tokens_limit']:,}", f"[{token_color}]{tokens_percent:.1f}%[/{token_color}]")
    
    console.print(table)
    
    # Show warnings if near limits
    if used_percent >= 80:
        show_warning(f"Budget at {used_percent:.0f}% — consider adjusting limits")
    if tokens_percent >= 80:
        show_warning(f"Token usage at {tokens_percent:.0f}% — approaching limit")

@app.command()
def set_limit(amount: float):
    """
    Set budget limit in dollars.
    
    Example:
        assistant budget set-limit 20.0
    """
    if amount <= 0:
        show_error("Limit must be positive")
        raise typer.Exit(1)
    
    _budget_state["limit"] = amount
    show_success(f"Budget limit set to ${amount:.2f}")

@app.command()
def set_token_limit(amount: int):
    """
    Set token limit.
    
    Example:
        assistant budget set-token-limit 2000000
    """
    if amount <= 0:
        show_error("Limit must be positive")
        raise typer.Exit(1)
    
    _budget_state["tokens_limit"] = amount
    show_success(f"Token limit set to {amount:,}")

@app.command()
def reset():
    """
    Reset usage counters.
    
    Example:
        assistant budget reset
    """
    _budget_state["used"] = 0
    _budget_state["tokens_used"] = 0
    show_success("Budget usage reset to zero")