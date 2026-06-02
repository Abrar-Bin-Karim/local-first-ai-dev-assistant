import typer

app = typer.Typer()


@app.command()
def explain(path: str):
    """
    Explain repository structure.
    """
    typer.echo(f"[REPO] Explaining repository: {path}")