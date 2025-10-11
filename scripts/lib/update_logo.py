import glob
import shutil

from PIL import Image


def update_logo(path_sep: str, cwd: str):
    # Get bin name from git config
    bin_name = ""
    with open(f"{cwd}{path_sep}.git{path_sep}config", "r") as f:
        content = f.read()

        # Try HTTPS format first
        if "url = https://github.com/" in content:
            try:
                user_name = content.split("url = https://github.com/")[1].split("/")[0]
                bin_name = content.split(f"url = https://github.com/{user_name}/")[
                    1
                ].split("\n")[0]
            except IndexError:
                pass

        # Try SSH format if HTTPS didn't work
        elif "url = git@github.com:" in content:
            try:
                user_name = content.split("url = git@github.com:")[1].split("/")[0]
                bin_name = content.split(f"url = git@github.com:{user_name}/")[1].split(
                    "\n"
                )[0]
            except IndexError:
                pass

        # Remove .git suffix if present
        if bin_name.endswith(".git"):
            bin_name = bin_name[:-4]

        # Convert to lowercase for binary name
        bin_name = bin_name.lower()

        # If we couldn't parse the name, raise an error
        if not bin_name:
            raise ValueError("Could not parse repository name from .git/config")

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
