#!/bin/bash

set -e

install_edm() {
    local EDM_MAJOR_MINOR="$(echo "$INSTALL_EDM_VERSION" | sed -E -e 's/([[:digit:]]+\.[[:digit:]]+)\..*/\1/')"
    local EDM_PACKAGE="edm_${INSTALL_EDM_VERSION}.pkg"
    local EDM_INSTALLER_PATH="${HOME}/.cache/download/${EDM_PACKAGE}"

    if [ ! -e "$EDM_INSTALLER_PATH" ]; then
        curl -o "$EDM_INSTALLER_PATH" -L "https://package-data.enthought.com/edm/osx_x86_64/${EDM_MAJOR_MINOR}/${EDM_PACKAGE}"
    fi

    sudo installer -pkg "$EDM_INSTALLER_PATH" -target /
}

install_edm
