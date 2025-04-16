import typer
from ask_git.commands import why, explain, pr_summary, summary

app = typer.Typer(help="Ask Git anything - powered by Ollama")

# Subcommands
#-------------

app.add_typer(why.app, name="why", help="Ask why a file, line, or feature changed.")
app.add_typer(summary.app, name="summary", help="Summarize changes over time.")
app.add_typer(explain.app, name="explain", help="Explain recent changes in a file.")
app.add_typer(pr_summary.app, name="pr-summary", help="Generate a summary of commits like a PR description.")

def main():
    app()

if __name__ == "__main__":
    main()
