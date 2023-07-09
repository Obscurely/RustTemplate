{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    rustup
    rustc
    cmake
    git
    gcc
    pkg-config
    python311Packages.pillow # this is for python repo script
  ];

  RUST_BACKTRACE = 1;
}
