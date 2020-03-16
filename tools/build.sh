#!/bin/bash
BASEDIR=$(realpath "$(dirname "${BASH_SOURCE[0]}")")
cd $BASEDIR/../
rm -rf ./build
git clone https://github.com/ajinabraham/NodeJsScan.git ./build
VERSION=`awk -v FS="VERSION = " 'NF>1{print $2}' $BASEDIR/../build/core/settings.py | tr -d '"'` 
docker build --label "version=$VERSION" -t nodejsscan-cli -f ./Dockerfile .
