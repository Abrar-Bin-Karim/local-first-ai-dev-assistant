import typer

app = typer.Typer()


@app.command()
def analyze(file: str):
    """
    Analyze log file.
    """
    typer.echo(f"[LOGS] Analyzing {file}")