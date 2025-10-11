import glob
import shutil

from lib.utils import parse_git_repo_info
from PIL import Image


def update_logo(path_sep: str, cwd: str):
    # Get bin name from git config
    _, repo_name = parse_git_repo_info(cwd, path_sep)
    bin_name = repo_name.lower()

    # Open base logo png file
    logo = Image.open(f"assets{path_sep}images{path_sep}logo.png")

    # Save it as ico
    logo.save(
        f"assets{path_sep}images{path_sep}logo.ico", format="ICO", size=[(256, 256)]
    )

    # Save it as icns
    logo.save(
        f"assets{path_sep}images{path_sep}logo.icns",
        format="ICNS",
        size=[(256, 256, 2)],
    )

    # Copy icns to macos folder
    macos_app_folder = glob.glob(f"resources{path_sep}macos{path_sep}*.app")[0]
    shutil.copyfile(
        f"assets{path_sep}images{path_sep}logo.icns",
        f"{macos_app_folder}{path_sep}Contents{path_sep}Resources"
        f"{path_sep}AppIcon.icns",
    )

    # Copy png logo to appdir linux folder
    linux_appdir = glob.glob(f"resources{path_sep}linux{path_sep}*.AppDir")[0]
    shutil.copyfile(
        f"assets{path_sep}images{path_sep}logo.png",
        f"{linux_appdir}{path_sep}{bin_name}.png",
    )

    # Resize png logo and copy to appdir & desktop folders
    sizes = [16, 32, 64, 128, 256, 512]

    # appdir folder
    with Image.open(f"assets{path_sep}images{path_sep}logo.png") as logo:
        for size in sizes:
            resized = logo.resize((size, size))
            resized.save(
                f"{linux_appdir}{path_sep}usr{path_sep}share{path_sep}icons"
                f"{path_sep}hicolor{path_sep}{size}x{size}{path_sep}apps"
                f"{path_sep}{bin_name}.png"
            )
            resized.save(
                f"resources{path_sep}linux{path_sep}desktop{path_sep}icons"
                f"{path_sep}hicolor{path_sep}{size}x{size}{path_sep}apps"
                f"{path_sep}{bin_name}.png"
            )
