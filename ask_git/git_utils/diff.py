from git import Repo

def get_diff_for_file(file_path: str, repo_path: str = ".") -> str:
    repo = Repo(repo_path)
    full_path = str(file_path)

    diffs = []

    # Unstaged changes (working tree)
    for diff_item in repo.index.diff(None, paths=full_path, create_patch=True):
        if diff_item.a_path == full_path or diff_item.b_path == full_path:
            diffs.append(diff_item.diff.decode("utf-8", errors="ignore"))

    # Staged changes
    for diff_item in repo.index.diff("HEAD", paths=full_path, create_patch=True):
        if diff_item.a_path == full_path or diff_item.b_path == full_path:
            diffs.append(diff_item.diff.decode("utf-8", errors="ignore"))

    # Untracked files
    if full_path in repo.untracked_files:
        try:
            with open(full_path, "r") as f:
                content = f.read()
            diffs.append(f"<<UNTRACKED FILE>>\n{content}")
        except Exception as e:
            diffs.append(f"<<UNTRACKED FILE BUT COULD NOT READ>> {e}")

    return "\n".join(diffs)