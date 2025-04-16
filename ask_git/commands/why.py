import typer

app = typer.Typer()

@app.command()
def main(
    file: str = typer.Argument(..., help="File to analyze"),
    line: int = typer.Option(None, help="Optional line number")
):
    """Explain why a file or line changed."""
    typer.echo(f"Analyzing: {file} (line: {line})")