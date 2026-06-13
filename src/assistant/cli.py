import typer
from assistant.commands import repo, git, logs, shell, budget, config

app = typer.Typer(help="Local First AI Developer Assistant")

# Register command groups
app.add_typer(repo.app, name="repo", help="Repository operations")
app.add_typer(git.app, name="git", help="Git operations")
app.add_typer(logs.app, name="logs", help="Log analysis")
app.add_typer(shell.app, name="shell", help="Shell command explanation")
app.add_typer(budget.app, name="budget", help="Budget management")
app.add_typer(config.app, name="config", help="Configuration")

@app.command()
def version():
    """Show version."""
    from rich.console import Console
    console = Console()
    console.print("[bold cyan]Assistant[/bold cyan] v0.1.0")

def main():
    app()

if __name__ == "__main__":
    main()