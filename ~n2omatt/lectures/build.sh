#!/bin/bash
################################################################################
## file   : build.sh                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
## Copy the lectures stuff to Output folder.                                  ##
################################################################################

## Change the directory to directory of the script.
## We need this because the script is written assuming that
## it's path is the CWD.
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
OLD_CWD=$PWD;

cd $SCRIPTPATH;

## Clean
rm -rf ./Output
mkdir -p ./Output

## Copy content
for NAME in $(ls .); do
    if [ -d "$NAME" ] && [ "$NAME" != "Output" ]; then
        cp -rf "$NAME" "./Output/$NAME"
    fi;
done;

## Restore the OLD CWD
cd $OLD_CWD
