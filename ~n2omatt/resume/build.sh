#!/bin/bash
################################################################################
## file   : build.sh                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
## Copy the resumes to Output folder.                                         ##
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
cp index_original.html ./Output/index.html


## Restore the OLD CWD
cd $OLD_CWD
