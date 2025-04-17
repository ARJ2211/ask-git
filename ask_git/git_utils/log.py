from git import Repo
from datetime import datetime
from typing import List, Dict, Optional


def get_commits(
        repo_path: str = ".", 
        max_count: Optional[int] = None,
        since: Optional[str] = None,
        until: Optional[str] = None,
        author: Optional[str] = None,
) -> List[Dict]:
    repo = Repo(repo_path)

    # Get all the commits on the current HEAD
    commits = repo.iter_commits(max_count=max_count)

    results = []
    for c in commits:
        # Filter by date
        commit_date = c.committed_date.date()
        if since and commit_date < datetime.strptime(since, r"Y-%m-%d"):
            continue
        if until and commit_date > datetime.strptime(until, r"%Y-%m-%d"):
            continue

        # Filter by author
        if author and author.lower() not in c.author.name.lower():
            continue

        results.append({
            "sha": c.hexsha,
            "message": c.message.strip(),
            "author": c.author.name,
            "date": c.committed_date.strftime(r"%Y-%m-%d %H:%M"),
            "diff": c.diff(None, create_patch=True)
        })
    
    return results
