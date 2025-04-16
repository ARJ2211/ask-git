from git import Repo

def get_diff_for_file(file_path: str, repo_path: str = ".") -> str:
    repo = Repo(repo_path)
    head_commit = repo.head.commit
    diff = head_commit.diff(None, paths=file_path, create_patch=True)

    for d in diff:
        if d.a_path == file_path or d.b_path == file_path:
            return d.diff.decode("utf-8", errors="ignore")
    
    return ""
