import os
from typing import List, Tuple


def get_target_files(cwd: str, path_sep: str) -> List[str]:
    """Get all target files that should be processed, excluding certain directories and file types."""
    skip_dirs = [
        f"{cwd}{path_sep}.git",
        f"{cwd}{path_sep}.mypy_cache",
        f"{cwd}{path_sep}assets",
        f"{cwd}{path_sep}fuzz{path_sep}artifacts",
        f"{cwd}{path_sep}fuzz{path_sep}corpus",
        f"{cwd}{path_sep}fuzz{path_sep}target",
        f"{cwd}{path_sep}scripts",
        f"{cwd}{path_sep}target",
        f"{cwd}{path_sep}docs",
    ]

    target_files = []

    for path, _, files in os.walk(cwd):
        stop = 0
        for dir in skip_dirs:
            if dir in path and ".github" not in path:
                stop = 1
                continue

        if stop == 1:
            continue

        for file in files:
            if (
                file != "Cargo.lock"
                and ".png" not in file
                and ".ico" not in file
                and ".icns" not in file
            ):
                target_files.append(os.path.join(path, file))

    return target_files


def parse_git_repo_info(cwd: str, path_sep: str) -> Tuple[str, str]:
    """Parse GitHub repository information from .git/config file."""
    repo_name = ""
    user_name = ""
    
    with open(f"{cwd}{path_sep}.git{path_sep}config", "r") as f:
        content = f.read()
        
        # Try HTTPS format first
        if "url = https://github.com/" in content:
            try:
                user_name = content.split("url = https://github.com/")[1].split("/")[0]
                repo_name = content.split(f"url = https://github.com/{user_name}/")[
                    1
                ].split("\n")[0]
            except IndexError:
                pass

        # Try SSH format if HTTPS didn't work
        elif "url = git@github.com:" in content:
            try:
                user_name = content.split("url = git@github.com:")[1].split("/")[0]
                repo_name = content.split(f"url = git@github.com:{user_name}/")[
                    1
                ].split("\n")[0]
            except IndexError:
                pass

        # Remove .git suffix if present
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]

        # If neither format worked, provide fallback or raise error
        if not user_name or not repo_name or user_name == "" or repo_name == "":
            raise ValueError(
                "Could not parse GitHub repository information from .git/config"
            )

    return user_name, repo_name
