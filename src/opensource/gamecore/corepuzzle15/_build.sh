#!/bin/bash

################################################################################
## CorePuzzle15 local build                                                      ##
################################################################################

## Copy the doxygen docs. ##

#Some vars...
SRC_DIR=$AMAZING_COW_PROJECTS_DIRECTORY/AmazingCow-Game-Core/CorePuzzle15
DST_DIR=$(pwd);

DOXYGEN_SRC=$SRC_DIR/doxygen
DOXYGEN_DST=$DST_DIR

#Genereate the doxygen docs locally...
cd $SRC_DIR

git pull --quiet origin master
$AMAZINGCOW_ENV_DOXYGEN Doxyfile >/dev/null 2>&1

git pull --quiet origin master
cd $DST_DIR >/dev/null 2>&1

#Copy to destination.
git pull --quiet origin master
cp -rf $DOXYGEN_SRC $DOXYGEN_DST >/dev/null 2>&1
