{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    llvmPackages_latest.llvm
    llvmPackages_latest.bintools
    zlib.out
    xorriso
    grub2
    llvmPackages_latest.lld
    rustup
    rustc
    cmake
    git
    gcc
    pkg-config
    python311
    python311Packages.pillow # this is for python repo script
  ];

  RUST_BACKTRACE = 1;
}
