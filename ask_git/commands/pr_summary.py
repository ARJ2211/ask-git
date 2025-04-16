import typer

app = typer.Typer()

@app.callback()
def main():
    """Generate PR-style summary of recent commits."""
    typer.echo("Generating PR-style commit summary")
