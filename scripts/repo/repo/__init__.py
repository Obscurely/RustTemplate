import os
import platform
import sys
from update_logo import update_logo
from init_repo import init_repo

# Get current directory
cwd = os.getcwd()

# Make sure we are in the root folder and not in the scripts folder
# + get the platform path separator \ for Windows and / for Linux.
path_sep = ""
if platform.system() == "Windows":
    path_split = cwd.split("\\")
    path_sep = "\\"
    if "repo" == path_split[-1]:
        path_split.pop()
        path_split.pop()
        os.chdir("\\".join(path_split))
else:
    path_split = cwd.split("/")
    path_sep = "/"
    if "repo" == path_split[-1]:
        path_split.pop()
        path_split.pop()
        os.chdir("/".join(path_split))

# Reset the current directory
cwd = os.getcwd()
print(cwd)

# get arguments
try:
    run_arg = sys.argv[1]
except IndexError:
    print("No arguments passed!")
    exit()

# Main script run
if run_arg == "init":
    init_repo(path_sep, cwd)
elif run_arg == "ulogo":
    update_logo(path_sep, cwd)
else:
    print("Argument not recognized!")
