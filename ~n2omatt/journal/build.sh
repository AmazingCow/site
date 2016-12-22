#!/bin/bash
################################################################################
## file   : build.sh                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
################################################################################

## Change the directory to directory of the script.
## We need this because the script is written assuming that
## it's path is the CWD.
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
OLD_CWD=$PWD;

cd $SCRIPTPATH;

rm -rf Output;
mkdir Output;

cp index_original.html Output/index.html
cp -R photos           Output/photos
cp -R img              Output/img

## Restore the OLD CWD
cd $OLD_CWD
