import typer

app = typer.Typer()


@app.callback()
def main():
    """
    Local First AI Dev Assistant
    """
    pass


@app.command()
def version():
    """
    Show version.
    """
    typer.echo("Assistant v0.1.0")


if __name__ == "__main__":
    app()