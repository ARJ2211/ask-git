from pathlib import Path

def is_git_repo(path=".") -> bool:
    return (Path(path) / ".git").exists()
