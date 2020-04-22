#!/bin/bash

set -e

install_edm() {
    local EDM_MAJOR_MINOR="$(echo "$INSTALL_EDM_VERSION" | sed -E -e 's/([[:digit:]]+\.[[:digit:]]+)\..*/\1/')"
    local EDM_PACKAGE="edm_cli_${INSTALL_EDM_VERSION}_linux_x86_64.sh"
    local EDM_INSTALLER_PATH="${HOME}/.cache/download/${EDM_PACKAGE}"

    if [ ! -e "$EDM_INSTALLER_PATH" ]; then
        curl -o "$EDM_INSTALLER_PATH" -L "https://package-data.enthought.com/edm/rh6_x86_64/${EDM_MAJOR_MINOR}/${EDM_PACKAGE}"
    fi

    bash "$EDM_INSTALLER_PATH" -b -p "${HOME}/edm"
}

install_edm
