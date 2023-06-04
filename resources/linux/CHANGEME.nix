{ lib, stdenv, appimageTools, desktop-file-utils, fetchurl }:

let
  version = "VERSION_PLACEHOLDER";
  name = "CHANGEME_BIN-${version}";

  plat = {
    x86_64-linux = "";
  }.${stdenv.hostPlatform.system};

  sha256 = {
    x86_64-linux = "SHA_PLACEHOLDER";
  }.${stdenv.hostPlatform.system};

  src = fetchurl {
    url = "https://github.com/Obscurely/CHANGEME_NAME/releases/download/v${version}-stable/CHANGEME_BIN-linux.AppImage";
    inherit sha256;
  };

  appimageContents = appimageTools.extractType2 {
    inherit name src;
  };
in
appimageTools.wrapType2 rec {
  inherit name src;

  extraInstallCommands = ''
    mkdir -p $out/share/pixmaps $out/share/licenses/CHANGEME_BIN
    cp ${appimageContents}/CHANGEME_BIN.png $out/share/pixmaps/
    cp ${appimageContents}/CHANGEME_NAME.desktop $out
    cp ${appimageContents}/LICENSE $out/share/licenses/CHANGEME_BIN/LICENSE
    mv $out/bin/${name} $out/bin/CHANGEME_BIN
    ${desktop-file-utils}/bin/desktop-file-install --dir $out/share/applications \
      --set-key Exec --set-value $out/bin/CHANGEME_BIN \
      --set-key Comment --set-value "CHANGEME_NAME Linux" \
      --delete-original $out/CHANGEME_NAME.desktop
  '';

  meta = {
    homepage = "https://github.com/Obscurely/CHANGEME_NAME";
    description = "CHANGEME_DESC";
    license = lib.licenses.mit;
    platforms = lib.platforms.linux;
  };
}
