#!/bin/sh
create-dmg \
	--volname CHANGEME_NAME \
	--volicon "../../assets/images/logo.icns" \
	--hide-extension "CHANGEME_NAME.app" \
	--background "../../assets/images/dmg-background.png" \
	--window-size 600 450 \
	--icon-size 94 \
	--icon "CHANGEME_NAME.app" 141 249 \
	--app-drop-link 458 249 \
	../../target/osx/CHANGEME_BIN-macos-installer.dmg \
	./CHANGEME_NAME.app
