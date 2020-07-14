#!/usr/bin/env bash
# requires bash >= 4.1

INSTALL_PATH="/opt/gmtii"
BACKUP_PATH="/home/gmtii/backup"
RELEASE_FILE="hezarbin.tar.gz"

#--------------------------------------

function is_running() {
    PIDS=`pidof hezarbin`
    if [ -n "$PIDS" ]; then
        echo "hezarbin is alreasy running as: ${PIDS}"
        echo "please stop it first by:"
        echo "  $> sudo systemctl stop hezarbin.service"
        exit 0
    fi
}

function make_backup() {
    echo "making a backup ..."
    mkdir -p ${BACKUP_PATH}
    FNAME=`date +%Y%m%d`
    FPATH="${BACKUP_PATH}/${FNAME}.tar.gz"
    [[ -f "${FPATH}" ]] && rm ${FPATH}
    tar czf ${FPATH} -C "${INSTALL_PATH}" .
    echo "a backup has been created as: ${FPATH}"
}

function clean_up() {
    rm -rf "${INSTALL_PATH}/config"
    rm -rf "${INSTALL_PATH}/www"
    rm -rf "${INSTALL_PATH}"/hezarbin*
}

function deploy() {
    echo "extracting ${RELEASE_FILE} into ${INSTALL_PATH} ..."
    tar xzf ${RELEASE_FILE} -C ${INSTALL_PATH}
    echo -e "\nnew release has been deployed"
}

#--------------------------------------

[[ -n "$1" ]] && RELEASE_FILE=$1

is_running
make_backup
clean_up
deploy
