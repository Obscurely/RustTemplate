{ lib, stdenv, appimageTools, desktop-file-utils, fetchurl }:

let
  version = "VERSION_PLACEHOLDER";
  name = "CHANGEME-${version}";

  plat = {
    x86_64-linux = "";
  }.${stdenv.hostPlatform.system};

  sha256 = {
    x86_64-linux = "SHA_PLACEHOLDER";
  }.${stdenv.hostPlatform.system};

  src = fetchurl {
    url = "https://github.com/Obscurely/CHANGEME/releases/download/v${version}-stable/CHANGEME-linux.AppImage";
    inherit sha256;
  };

  appimageContents = appimageTools.extractType2 {
    inherit name src;
  };
in
appimageTools.wrapType2 rec {
  inherit name src;

  extraInstallCommands = ''
    mkdir -p $out/share/pixmaps $out/share/licenses/CHANGEME
    cp ${appimageContents}/CHANGEME.png $out/share/pixmaps/
    cp ${appimageContents}/CHANGEME.desktop $out
    cp ${appimageContents}/LICENSE $out/share/licenses/CHANGEME/LICENSE
    mv $out/bin/${name} $out/bin/CHANGEME
    ${desktop-file-utils}/bin/desktop-file-install --dir $out/share/applications \
      --set-key Exec --set-value $out/bin/CHANGEME \
      --set-key Comment --set-value "CHANGEME Linux" \
      --delete-original $out/CHANGEME.desktop
  '';

  meta = {
    homepage = "https://github.com/Obscurely/CHANGEME";
    description = "CHANGEME";
    license = lib.licenses.mit;
    platforms = lib.platforms.linux;
  };
}
