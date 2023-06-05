{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    rustup
    rustc
    cmake
    git
    gcc
    pkg-config
  ];

  RUST_BACKTRACE = 1;
}
