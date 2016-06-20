#!/bin/bash

################################################################################
## libstdcow local build                                                      ##
################################################################################

## Copy the doxygen docs. ##

#Some vars...
SRC_DIR=$AMAZING_COW_PROJECTS_DIRECTORY/AmazingCow-Libs/libstdcow
DST_DIR=$(pwd);

DOXYGEN_SRC=$SRC_DIR/doxygen
DOXYGEN_DST=$DST_DIR

#Genereate the doxygen docs locally...
cd $SRC_DIR
doxygen Doxyfile > /dev/null
git pull --quiet origin master
cd $DST_DIR >/dev/null 2>&1

#Copy to destination.
git pull --quiet origin master
cp -rf $DOXYGEN_SRC $DOXYGEN_DST >/dev/null 2>&1
