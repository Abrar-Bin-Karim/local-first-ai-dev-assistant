import typer

app = typer.Typer()


@app.command()
def history():
    """
    Show git history.
    """
    typer.echo("[GIT] History not implemented yet")