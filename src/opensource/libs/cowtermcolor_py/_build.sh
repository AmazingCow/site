#!/bin/bash

################################################################################
## CoreClock local build                                                      ##
################################################################################

## Copy the doxygen docs. ##

#Some vars...
SRC_DIR=$AMAZING_COW_PROJECTS_DIRECTORY/AmazingCow-Libs/cowtermcolor_py
DST_DIR=$(pwd);

PYDOC_SRC=$SRC_DIR/pydoc
PYDOC_DST=$DST_DIR

#Genereate the pydoc docs locally...
cd $SRC_DIR
pydoc -w cowtermcolor
mkdir -p pydoc
mv cowtermcolor.html pydoc/index.html
git pull --quiet origin master
cd $DST_DIR >/dev/null 2>&1

#Copy to destination.
cp -rf $PYDOC_SRC $PYDOC_DST
