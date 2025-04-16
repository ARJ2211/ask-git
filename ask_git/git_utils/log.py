from git import Repo
from typing import List

def get_commits(repo_path: str = ".", max_count: int = 10) -> List[str]:
    repo = Repo(repo_path)
    return [c.message.strip() for c in repo.iter_commits(max_count=max_count)]
