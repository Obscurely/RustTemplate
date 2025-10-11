
from lib.utils import get_target_files


def update_desc(path_sep: str, cwd: str):
    # Load desc
    desc = ""
    with open(f"scripts{path_sep}data{path_sep}DESC", "r") as f:
        desc = f.read().replace("\n", "")

    # Get all the files we want to manipulate with their full paths.
    target_files = get_target_files(cwd, path_sep)

    for file in target_files:
        content = ""

        with open(file, "r") as f:
            content = f.read()

        content = content.replace("CHANGEME_DESC", desc)

        with open(file, "w") as f:
            f.write(content)
