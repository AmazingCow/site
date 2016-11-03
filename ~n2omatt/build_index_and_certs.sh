#!/bin/bash
################################################################################
## file   : build.sh                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
## Create the certifications images and html pages.                           ##
## Update the index with the output of certifications.                        ##
################################################################################

## Change the directory to directory of the script.
## We need this because the script is written assuming that
## it's path is the CWD.
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
OLD_CWD=$PWD;


## Update the Certifications.
cd $SCRIPTPATH;
cd ./_build_stuff/MyCerts;
git pull origin master

# Build the Certifications.
cd $SCRIPTPATH;
cd ./_build_stuff/certification_scripts;
./generate_certifications.sh;
