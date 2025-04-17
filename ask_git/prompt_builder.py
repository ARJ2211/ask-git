def build_explain_prompt(
    file: str,
    line_start: int,
    line_end: int,
    diff: str,
    blame_lines: list[tuple[int, str, str]]
) -> str:
    prompt = f"""
        You are a helpful AI code reviewer. 
        Explain why the following lines in the file `{file}` might have changed.

        Line range: {line_start} to {line_end}

        Here is the Git diff:
        {diff}
    """

    if blame_lines:
        prompt += "\nHere is the Git blame (who last edited each line):\n"
        for lineno, author, content in blame_lines:
            prompt += f"• Line {lineno} by {author}: {content.strip()}\n"
    else:
        prompt += "\nNo blame information was available for these lines, but you should still analyze the diff and explain the reasoning behind the changes. The different diff blocks need to be explain block by block"

    prompt += "\n\nRespond with a concise explanation of why these lines may have changed."
    return prompt


def build_summary_prompt():
    pass
