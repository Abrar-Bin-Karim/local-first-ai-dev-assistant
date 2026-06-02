import typer

from assistant.commands import (
    repo,
    git,
    logs,
    shell,
    budget
)

app = typer.Typer(
    help="Local First AI Developer Assistant"
)

app.add_typer(repo.app, name="repo")
app.add_typer(git.app, name="git")
app.add_typer(logs.app, name="logs")
app.add_typer(shell.app, name="shell")
app.add_typer(budget.app, name="budget")


@app.command()
def version():
    """Show version"""
    typer.echo("Assistant v0.1.0")


if __name__ == "__main__":
    app()