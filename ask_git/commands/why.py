import typer
from pathlib import Path

from ask_git.git_utils.diff import get_diff_for_file
from ask_git.git_utils.blame import get_blame_for_file
from ask_git.git_utils.utils import get_relative_path_from_repo_root

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

    # Print analysis context message
    message = f"🔍 Analyzing changes in: {path}"
    if line_end and not line_start:
        typer.echo("❌ Line end given but no line start.")
        raise typer.Exit()
    elif line_start and not line_end:
        message += f" (starting from line {line_start})"
    elif line_start and line_end:
        message += f" (lines {line_start} to {line_end})"
    typer.echo(message)

    # Get relative path to repo root for GitPython diff
    relative_path = get_relative_path_from_repo_root(path)

    # Get full diff for the file
    diff = get_diff_for_file(str(relative_path))
    if not diff:
        typer.echo("⚠️ No diffs found for this file.")
        return

    # Show the full diff (line range slicing skipped)
    typer.echo(
        f"\n📄 Git Diff (full file shown, selected lines "
        "{line_start}-{line_end or line_start}):\n"
    )
    typer.echo(diff)

    # Show blame output if line_start is provided
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
