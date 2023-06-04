{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    rustc
    cmake
    git
    gcc
    pkg-config
  ];

  RUST_BACKTRACE = 1;
}
