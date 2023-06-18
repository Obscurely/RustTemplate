import os
import platform

# Get current directory
cwd = os.getcwd()

# Make sure we are in the root folder and not in the scripts folder
# + get the platform path separator \ for Windows and / for Linux.
path_sep = ""
if platform.system() == "Windows":
    path_split = cwd.split("\\")
    path_sep = "\\"
    if "scripts" == path_split[-1]:
        path_split.pop()
        os.chdir("\\".join(path_split))
else:
    path_split = cwd.split("/")
    path_sep = "/"
    if "scripts" == path_split[-1]:
        path_split.pop()
        os.chdir("/".join(path_split))

# Reset the current directory
cwd = os.getcwd()

# Directories we can ignore
skip_dirs = [
    f"{cwd}{path_sep}.git",
    f"{cwd}{path_sep}.mypy_cache",
    f"{cwd}{path_sep}assets",
    f"{cwd}{path_sep}fuzz{path_sep}artifacts",
    f"{cwd}{path_sep}fuzz{path_sep}corpus",
    f"{cwd}{path_sep}fuzz{path_sep}target",
    f"{cwd}{path_sep}target",
]

# Get all the files we want to manipulate with their full paths.
target_files = []

for path, _, files in os.walk(cwd):
    stop = 0
    for dir in skip_dirs:
        if dir in path:
            stop = 1
            continue

    if stop == 1:
        continue

    for file in files:
        if file != "Cargo.lock":
            target_files.append(os.path.join(path, file))

# Get user name and repo name
repo_name = ""
user_name = ""
with open(f"{cwd}{path_sep}.git{path_sep}config", "r") as f:
    content = f.read()
    user_name = content.split("url = https://github.com/")[1].split("/")[0]
    repo_name = content.split(f"url = https://github.com/{user_name}/")[1].split("\n")[
        0
    ]

# Get primary email address
pmail = ""
with open(f"{cwd}{path_sep}scripts{path_sep}PMAIL", "r") as f:
    pmail = f.readlines()[0].replace("\n", "")

# Get secondary email address
smail = ""
with open(f"{cwd}{path_sep}scripts{path_sep}SMAIL", "r") as f:
    smail = f.readlines()[0].replace("\n", "")

# Create a dictionary with the vars
vars = {
    "CHANGEME_USER": user_name,
    "CHANGEME_NAME": repo_name,
    "CHANGEME_BIN": repo_name.lower(),
    "CHANGEME_PMAIL": pmail,
    "CHANGEME_SMAIL": smail,
}

for file in target_files:
    content = ""
    with open(file, "r") as f:
        content = f.read()

    for var in vars:
        content.replace(var, vars[var])

    with open(file, "w") as f:
        f.write(content)
