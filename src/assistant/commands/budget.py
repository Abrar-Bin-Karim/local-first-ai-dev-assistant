import typer

app = typer.Typer()


@app.command()
def status():
    """
    Show budget status.
    """
    typer.echo("[BUDGET] Current budget status")