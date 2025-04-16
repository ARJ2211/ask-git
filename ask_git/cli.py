import typer
from ask_git.commands import why, explain, pr_summary, summary

app = typer.Typer(help="Ask Git anything - powered by Ollama")

# Register Commands
#------------------

app.command(name="explain")(explain.main)
app.command(name="why")(why.main)
app.command(name="summary")(summary.main)
app.command(name="pr_summary")(pr_summary.main)

def main():
    app()

if __name__ == "__main__":
    main()
