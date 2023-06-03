<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="assets/logo.png" alt="Logo" width="150" height="150">

<h1 align="center"></h1>

<p align="center">
    An open source, cross-platform, programmed in rust, encrypted digital vault (store files and text) with the capability to set a path and
    with the click of a button to copy the content to that file. For example store your ssh keys safely, put your vault in like your github dotfiles,
    download it on another machine and easily install those keys.
    <br />
    <a href="https://github.com/Obscurely/EStash/issues">Report Bug</a>
    |
    <a href="https://github.com/Obscurely/EStash/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#video-showcase">Video showcase</a></li>
        <li><a href="#built-with">Built with</a></li>
        <ul>
          <li><a href="#the-stock-libraries-and-these-awesome-3rd-party-ones">The stock libraries and these awesome 3rd party ones</a></li>
        </ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#running-the-program">Running the Program</a></li>
        <ul>
          <li><a href="#windows">Windows</a></li>
          <ul>
            <li><a href="#portable-exe">Portable EXE</a></li>
            <li><a href="#installer">Installer</a></li>
          </ul>
          <li><a href="#linux">Linux</a></li>
          <ul>
            <li><a href="#portable-bin">Portable Bin</a></li>
            <li><a href="#appimage">AppImage</a></li>
            <li><a href="#aur">AUR</a></li>
            <li><a href="#nix-file">Nix File</a></li>
            <li><a href="#deb-file">Deb File</a></li>
            <li><a href="#arch-pkg-file">Arch Pkg File</a></li>
          </ul>
          <li><a href="#macos">MacOS</a></li>
          <ul>
            <li><a href="#portable-binary">Portable Bin</a></li>
            <li><a href="#app-folder">App Folder</a></li>
            <li><a href="#dmg-installer">DMG Installer</a></li>
            <li><a href="#homebrew">Homebrew</a></li>
          </ul>
          <li><a href="#all-platforms">All Platforms</a></li>
        </ul>
        <li><a href="#compilation">Compilation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#basics">Basics</a></li>
        <ul>
          <li><a href="#login">Login</a></li>
          <li><a href="#the-vault">The Vault</a></li>
        </ul>
        <li><a href="#advanced">Advanced</a></li>
      </ul>
    </li>
    <li><a href="#road-map">Road Map</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## 🪽 About The Project

- An open source, programmed in rust, encrypted digital vault (store files and
  text) with the capability to set a path and with the click of a button to copy
  the content to that file. For example store your ssh keys safely, put your
  vault in like your github dotfiles, download it on another machine and easily
  install those keys.<br>
- The vault is encrypted using a key derived from your password (the strength of
  your password decides the safetyness of your vault) using argon2id and that
  key is used to encrypt the private key. The encryption algorithm used is an
  ECIES, combines X25519 Diffie-Hellman function and XChaCha20Poly1305. (I used
  an
  [ECIES](https://itecspec.com/spec/3gpp-33-501-c-3-elliptic-curve-integrated-encryption-scheme-ecies/)
  for future proof reasons as there are no security downsides)
- The way this works is by hashing your vault name with blake3. The password
  doesn't get stored, but a key derived from your password of 32 bytes length
  using argon2id gets generated with some very strong options and with this key
  the private encryption key for the vault (from the ECIES) get's encrypted. You
  get logged into a vault if the private key is decrypted sucessfully and the
  vault name is present basically. And all the content inside a vault is
  encrypted using the key-pair for that vault, basically nothing gets leaked.

### 🎥 Video showcase

https://user-images.githubusercontent.com/59087558/206248579-a786b277-b0fc-4306-be50-9db1c948e901.mp4

### 🍔 Built with

- [Rust 1.64.0](https://www.rust-lang.org/)

#### The stock libraries and these awesome 3rd party ones:

- [BLAKE3](https://lib.rs/crates/blake3) hash function, much faster then sha2
  and more secure.
- [rust-argon2](https://lib.rs/crates/rust-argon2) for deriving the encryption
  key from the password.
- [rand](https://lib.rs/crates/rand) random number generators and other
  randomness functionality.
- [rand_hc](https://lib.rs/crates/rand_hc) HC128 random number generator.
- [zeroize](https://lib.rs/crates/zeroize) securely clear secrets from memory
  with a simple trait.
- [crypto_box](https://lib.rs/crates/crypto_box)
  [ECIES](https://itecspec.com/spec/3gpp-33-501-c-3-elliptic-curve-integrated-encryption-scheme-ecies/)
  that combines X25519 Diffie-Hellman function and XChaCha20Poly1305.
- [chacha20poly1305](https://lib.rs/crates/chacha20poly1305) simple, fast and
  strong [AEAD](https://en.wikipedia.org/wiki/Authenticated_encryption)
  encryption algorithm.
- [sled](https://lib.rs/crates/sled) lightweight high-performance pure-rust
  transactional embedded database.
- [Serde](https://lib.rs/crates/serde) a generic serialization/deserialization
  framework.
- [serde_json](https://lib.rs/crates/serde_json) a JSON serialization file
  format.
- [FLTK](https://lib.rs/crates/fltk) rust bindings for the FLTK GUI library.
- [dirs](https://lib.rs/crates/dirs) a tiny low-level library that provides
  platform-specific standard locations.

## 🏁 Getting Started

### 🏃‍♂️ Running The Program

- [Windows](#windows)
- [Linux](#linux)
- [MacOS](#macos)
- [All Platforms](#all-platforms)

---

### 🪟 Windows

- [Portable EXE](#portable-exe)
- [Installer](#installer)

#### Portable EXE

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-windows.exe_ file (might have to click show all).
2. Double click the exe you just downloaded and there you go the program works.
3. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

#### Installer

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-windows-installer.exe_ files (might have to click show
   all).
2. Double click the installer and go through the it as you would with any other
   installer.
3. If you look now in the start menu (or on the desktop if you ticked create
   desktop shortcut) you are gonna see a shortcut for estash, just run it like
   any other program.
4. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

---

### 🐧 Linux

- [Portable Bin](#portable-bin)
- [AppImage](#appimage)
- [AUR](#aur)
- [Nix File](#nix-file)
- [Deb File](#deb-file)
- [Arch Pkg File](#arch-pkg-file)

#### Portable Bin

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-linux_ file.
2. Double click the bin you just downloaded and there you go the program works.
3. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

#### AppImage

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-linux.AppImage_ file.
2. Double click the AppImage you download and there you go the program just
   works. You may want to install
   [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher) if you
   don't have it already, when you start the AppImage you'll get a prompt asking
   if you want to integrate and run it and if you do so it will appear just as
   if you installed it.
3. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

#### AUR

The PKGs are: estash (for stable), estash-bin (for precompiled) and estash-git
(to compile latest source code)

a. if you have an AUR manager (like
[paru](https://github.com/Morganamilo/paru/blob/master/README.md#installation)
or [yay](https://github.com/Jguer/yay/blob/next/README.md#installation), which
you should)

1. Just like with any other AUR pkg choose your prefered type and you can run
   the following command for example.

```shell
paru -Sy estash
```

2. Search for estash in your app launcher and launch it.
3. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

b. Manually cloning and building it from AUR

1. First install the basic build dependencies, if you don't already have them:

```shell
sudo pacman -Sy gcc base-devel --needed
```

2. Then clone the build script

```shell
git clone https://aur.archlinux.org/estash.git # or estash-bin & estash-git
```

3. Cd into the new cloned repository and run the following to build the package

```shell
makepkg
```

4. In order to install the package run the following (where \* is just an any
   other characters place holder)

```shell
sudo pacman -U estash-*.pkg.tar.zst
```

#### Nix File

You are using NixOS, don't worry I got you bro.

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-linux.nix_ file.
2. If you use flakes then put it in your pkgs folder, and up-top add your tag
   (like _my_). If you don't just add the code in your default.nix file and
   install it this way.
3. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

#### Deb File

You should use the app image. This does not provide a desktop file, you'll have
to run it from the command line. It's here just as another means if needed. I
will try to make a ppa.

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-linux.deb_ file.
2. Open a terminal in the folder where your download is and run the following
   command:

```shell
sudo dpkg -i estash-linux.deb
```

3. Run _estash_ in the terminal and there it is, the app.
4. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

#### Arch Pkg File

You shouldn't use this method, install the estash-bin AUR pkg instead. This is
here just as another means if needed.

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-linux.pkg.tar.zst_ file.
2. From you Arch Linux command line run the following command:

```shell
sudo pacman -U estash-linux.pkg.tar.zst
```

3. Search for estash in your app launcher and launch it.
4. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

---

### 🍎 MacOS

- [Portable binary](#portable-binary)
- [App Folder](#app-folder)
- [DMG Installer](#dmg-installer)
- [Homebrew](#homebrew)

#### Portable binary

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-macos_ file.
2. Double click the bin you just downloaded and there you go the program works.
3. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

#### App Folder

Very simillar to [portable binary](#portable-binary), only real difference is
this has an icon.

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-macos-app.tar.gz_ file.
2. Use your archive manager or run in the terminal the following command:

```shell
tar -xzf estash-macos-app.tar.gz
```

3. Double clikc the app folder you just downloaded and there you go the program
   works.
4. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

#### DMG Installer

Works just like any other dmg installer you've used.

1. Go to the [Releases Tab](https://github.com/Obscurely/EStash/releases) and
   download the _estash-macos-installer.dmg_ file.
2. Double click to run the dmg.
3. Drag the app folder over the _Applications_ folder.
4. Done, you've just installed the app, should see it in launchpad now.
5. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

#### Homebrew

Note this method doesn't come with a desktop entry. You'll have to run the
_estash_ command or just
[create a shortcut yourself](https://siytek.com/macos-terminal-command-as-a-shortcut/#2.-Create-a-new-shortcut),
it's really easy.

1. You will need to have [homebrew](https://brew.sh) installed, if you don't
   have it installed run the following command:

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. You'll need to add my tap repo, run the following command for that:

```shell
brew tap Obscurely/tap
```

3. Install the pkg.

```shell
brew install estash
```

4. Might wanna take a look at the [Usage Tab](usage) if you don't understand
   something about it.

---

### 🚉 All Platforms

This method will work across any Linux distribution, Windows 10/11 and macOS
(Big Sur+ tested).

1. Install rust, either using the official
   [rustup installer](https://www.rust-lang.org/tools/install) or any pkg
   manager you may use. (There is also a shell.nix file in the repo if you use
   nix)
2. Run the following command in your terminal of choice:

```shell
cargo install estash
```

3. Make sure you have .cargo/bin in path, for linux and macOS you would need to
   add the following line in your terminal RC file (e.g $HOME/.zshrc)

```shell
export PATH=$HOME/.cargo/bin:$PATH # This is for Linux & macOS, look below for Windows.
```

On windows it should work automatically (restart if just installed), if not you
can follow this [guide](https://www.computerhope.com/issues/ch000549.htm) for
how to add something to path. The cargo bin folder will be
{your-user-folder}\\.cargo\\bin

4. You may want to create a
   [symlink](https://www.freecodecamp.org/news/symlink-tutorial-in-linux-how-to-create-and-remove-a-symbolic-link/)
   on Linux & macOS or
   [create a shortcut](https://support.microsoft.com/en-us/office/create-a-desktop-shortcut-for-an-office-program-or-file-9a8df64b-cd87-4700-95cc-4bc3e2a962da)
   if you are on Windows to the bin file for easy access.

5. In order to update run the install command again, and you can now follow
   [usage](#usage) for more information on how to use it.

---

### 🛠️ Compilation

This program only uses cross platform libraries. The following steps require
that you have rust installed, check their official
[installation page](https://www.rust-lang.org/tools/install) or use any pkg
manager you may want. (There is also a shell.nix file in the repo if you use
nix).

1. Clone this repo on your PC, you can use "git clone", if you have git
   installed, like this:

```shell
git clone https://github.com/Obscurely/estash.git
```

Otherwise in the right up side of the repo page you will see a download button,
download the repo as zip and extract it in a folder

2. Open a new terminal/cmd window in the folder you extracted the repo in, if
   you can't right click on the folder and open it there do:

```shell
cd the/path
```

and you will get there.

3. From there run this compile command in the terminal:

```shell
cargo build --release
```

It will take a bit depending on your system because of executable size
optimizations, but be patient.

4. Done, navigate to target/release and grab only the "estash" file from there.

## 🪧 Usage

**In the provided [video](#video-showcase) it's presented everything you should
know on how to use EStash. I also think the UI is intuitive enough, but I
obviously can't have an unbiased opinion or a first look experience, so here you
go.**

### Basics

#### Login

1. First click on signup. The first field is the name of the vault, the second
   field is the password, and the third one is to verify the password. After
   inputting you desired credentials (note you can also make a vault with
   nothing as the vault name and password) click Singup and wait.
2. After the vault has been created in left up corner you will se a back arrow,
   click that.
3. Now that we are in the main menu click on Login. The first field is the name
   of the vault and the second one is the password. After inputting your
   credentials hit Login.

#### The Vault

- Add an entry by adding some text in the left down corner box and hitting the
  plus sign besides it.
- Get the content of an entry by clicking on its name in the tree
- Hit the plus/minus sign besides the install path box if you want to
  enable/disable the install path. The install path is checked if it's working
  on you current operating system.
- The Check button besides the install path box checks if the path is valid on
  your current operating system.
- The Content box represents what you would want to store, you can write
  anything utf-8 here, if it's not the UI will not let you do it so you don't
  have to worry about this.
- The Clear Content button simply clears anything in the content box.
- The Select File button let's you select a file from you system, any file,
  using the native file selecter or the one packaged with FLTK if none is found,
  and import all of its content inside the contents box. If the file is too big
  or is not in utf-8 format (for example it's a photo) the content box will be
  disabled and a message will you up and the file will automatically be stored
  in the entry.
- The Notes box has no real effect on the functionallity, if you want to add
  anything extra just write it there.
- The Delete button deletes the entry without question
- The Install button takes the contents of the content box even if you've
  modified it and not saved it and tries installing it to the desired install
  path if the install path is enabled.
- The Save button will simply save the entry, encrypted, to the db.

### Advanced

- Change the install path or add one without saving the entry, you may want this
  as an one time use.
- Change the content without saving the entry and installing that to a file.

## 🛣️ Road Map

The roadmap (kanban board) is located up top in the projects tab or at
[this link](https://github.com/users/Obscurely/projects/1).

## 💁 Contributing

Please read
[CONTRIBUTING.md](https://github.com/Obscurely/EStash/blob/master/CONTRIBUTING.md),
but to generalise it the basic process is: edit a file you want, do a
[pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request),
I will look at it and if the change makes sense and is a good one I will accept
it and that's it.

## 🪪 License

Is under [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html) so stick to the
license conditions and have fun :)</br>

## 📧 Contact

Either post an issue in the
[Issues Tab](https://github.com/Obscurely/falion/issues) or contact me at this
email adddress if you have more to say: obscurely.social@protonmail.com

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K3H29LV)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Obscurely/EStash.svg?style=for-the-badge
[contributors-url]: https://github.com/Obscurely/EStash/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Obscurely/EStash.svg?style=for-the-badge
[forks-url]: https://github.com/Obscurely/EStash/network/members
[stars-shield]: https://img.shields.io/github/stars/Obscurely/EStash.svg?style=for-the-badge
[stars-url]: https://github.com/Obscurely/EStash/stargazers
[issues-shield]: https://img.shields.io/github/issues/Obscurely/EStash.svg?style=for-the-badge
[issues-url]: https://github.com/Obscurely/EStash/issues
[license-shield]: https://img.shields.io/github/license/Obscurely/EStash.svg?style=for-the-badge
[license-url]: https://github.com/Obscurely/EStash/blob/master/LICENSE
