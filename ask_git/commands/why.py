import typer
from pathlib import Path

from ask_git.git_utils.diff import get_diff_for_file
from ask_git.git_utils.blame import get_blame_for_file

app = typer.Typer()

@app.command()
def main(
    file: str = typer.Argument(..., help="File to analyze"),
    line_start: int = typer.Option(None, help="Optional start line number"),
    line_end: int = typer.Option(None, help="Optional end line number")
):
    """Explain why a file or a range of lines changed."""
    path = Path(file).resolve()

    if not path.exists():
        typer.echo(f"❌ File path '{path}' does not exist!")
        raise typer.Exit()

    message = f"🔍 Analyzing changes in: {path}"
    if line_end and not line_start:
        typer.echo("❌ Line end given but no line start.")
        raise typer.Exit()
    elif line_start and not line_end:
        message += f" (starting from line {line_start})"
    elif line_start and line_end:
        message += f" (lines {line_start} to {line_end})"
    typer.echo(message)

    # Get the full diff
    diff = get_diff_for_file(str(path))
    if not diff:
        typer.echo("⚠️ No diffs found for this file.")
        return

    # If line range is specified, filter only those lines from the diff
    if line_start and line_end:
        selected_lines = []
        for i, line in enumerate(diff.splitlines(), start=1):
            if line_start <= i <= line_end:
                selected_lines.append(line)

        if not selected_lines:
            typer.echo("⚠️ No diff lines found within the specified range.")
        else:
            typer.echo(f"\n📄 Git Diff (lines {line_start}-{line_end}):\n")
            typer.echo("\n".join(selected_lines))
    else:
        typer.echo("\n📄 Full Git Diff:\n")
        typer.echo(diff)

    # Show blame if line_start is given
    if line_start:
        blame = get_blame_for_file(str(path))
        typer.echo(f"\n📌 Blame for lines {line_start} to {line_end or line_start}:\n")
        found = False
        for commit, lines in blame:
            for idx, content in enumerate(lines):
                lineno = idx + 1
                if line_start <= lineno <= (line_end or line_start):
                    found = True
                    typer.echo(f"• Line {lineno} by {commit.author.name}: {content.strip()}")
        if not found:
            typer.echo("⚠️ No matching lines found in blame output.")
