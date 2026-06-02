import typer

app = typer.Typer()


@app.command()
def explain(command: str):
    """
    Explain shell command.
    """
    typer.echo(f"[SHELL] Explaining: {command}")