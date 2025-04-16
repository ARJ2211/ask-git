import typer

app = typer.Typer()

@app.command()
def main(
    since: str = typer.Option(..., help="Start date (e.g., '2024-01-01')"),
    until: str = typer.Option(None, help="End date (default: today)")
):
    """Summarize commits in a date range."""
    typer.echo(f"Summarizing from {since} to {until}")
