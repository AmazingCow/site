#!/bin/bash

################################################################################
## Variables                                                                  ##
################################################################################
OUT_DIR="_Output/docs";
BASE_DIR="amazingcow_repos";


################################################################################
## Script                                                                     ##
################################################################################
echo "--> Creating projects directories";
mkdir -p $OUT_DIR;

## We create a directory on output folder for each
## project that we fetched from github.
for ORG_NAME in $(ls $BASE_DIR); do
    ORG_DIR=$BASE_DIR/$ORG_NAME;
    for PROJECT_NAME in $(ls $ORG_DIR); do
        PROJECT_DIR=$OUT_DIR/$PROJECT_NAME;
        mkdir -vp $PROJECT_DIR;
    done;
done;
