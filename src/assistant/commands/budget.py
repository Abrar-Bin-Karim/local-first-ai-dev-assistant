"""Token and cost management commands."""

import typer
from rich.console import Console
from rich.table import Table
from assistant.utils.ui import show_header, show_info, show_warning, show_success, show_error
from assistant.utils.config import Config

console = Console()
app = typer.Typer()
config = Config()  # persistent config

# Keys in the config
BUDGET_USED_KEY = "budget_used"
BUDGET_LIMIT_KEY = "budget_limit"
TOKENS_USED_KEY = "tokens_used"
TOKENS_LIMIT_KEY = "token_limit"

def _get_budget_state():
    """Load budget state from config."""
    return {
        "used": config.get(BUDGET_USED_KEY, 0.0),
        "limit": config.get(BUDGET_LIMIT_KEY, 10.0),
        "tokens_used": config.get(TOKENS_USED_KEY, 0),
        "tokens_limit": config.get(TOKENS_LIMIT_KEY, 1000000),
    }

def _save_budget_state(state):
    """Save budget state to config."""
    config.set(BUDGET_USED_KEY, state["used"])
    config.set(BUDGET_LIMIT_KEY, state["limit"])
    config.set(TOKENS_USED_KEY, state["tokens_used"])
    config.set(TOKENS_LIMIT_KEY, state["tokens_limit"])

@app.command()
def status():
    """Show current budget and token usage."""
    state = _get_budget_state()
    show_header("Budget Status")

    used_percent = (state["used"] / state["limit"]) * 100 if state["limit"] > 0 else 0
    tokens_percent = (state["tokens_used"] / state["tokens_limit"]) * 100 if state["tokens_limit"] > 0 else 0

    table = Table(title="Usage Summary")
    table.add_column("Resource", style="cyan")
    table.add_column("Used", style="yellow")
    table.add_column("Limit", style="green")
    table.add_column("Usage", style="white")

    cost_color = "green" if used_percent < 50 else "yellow" if used_percent < 80 else "red"
    token_color = "green" if tokens_percent < 50 else "yellow" if tokens_percent < 80 else "red"

    table.add_row("💰 Budget", f"${state['used']:.2f}", f"${state['limit']:.2f}", f"[{cost_color}]{used_percent:.1f}%[/{cost_color}]")
    table.add_row("🎫 Tokens", f"{state['tokens_used']:,}", f"{state['tokens_limit']:,}", f"[{token_color}]{tokens_percent:.1f}%[/{token_color}]")

    console.print(table)

    if used_percent >= 80:
        show_warning(f"Budget at {used_percent:.0f}% — consider adjusting limits")
    if tokens_percent >= 80:
        show_warning(f"Token usage at {tokens_percent:.0f}% — approaching limit")

@app.command()
def set_limit(amount: float):
    """Set budget limit in dollars."""
    if amount <= 0:
        show_error("Limit must be positive")
        raise typer.Exit(1)
    state = _get_budget_state()
    state["limit"] = amount
    _save_budget_state(state)
    show_success(f"Budget limit set to ${amount:.2f}")

@app.command()
def set_token_limit(amount: int):
    """Set token limit."""
    if amount <= 0:
        show_error("Limit must be positive")
        raise typer.Exit(1)
    state = _get_budget_state()
    state["tokens_limit"] = amount
    _save_budget_state(state)
    show_success(f"Token limit set to {amount:,}")

@app.command()
def reset():
    """Reset usage counters."""
    state = _get_budget_state()
    state["used"] = 0.0
    state["tokens_used"] = 0
    _save_budget_state(state)
    show_success("Budget usage reset to zero")

# Helper function for other modules to record usage
def record_usage(cost: float, tokens: int):
    """Called by LLM modules to update budget."""
    state = _get_budget_state()
    state["used"] += cost
    state["tokens_used"] += tokens
    _save_budget_state(state)
    