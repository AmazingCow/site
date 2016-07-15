#!/bin/bash

## Vars
TARGET_DIR=$1;
if [ -z "$TARGET_DIR" ]; then
    TARGET_DIR="./build";
fi;

ORIGINAL_CWD=$(pwd);


# Download the repositories if needed.
./download_amazingcow.py

## Build the Doxygen docs in each repo.
cd ./repos
for DIR in $(ls); do
    echo $DIR;
    cd $DIR;
    pwd;
    doxygen
    cd ..
done;

## Create the projects dir that will hold
## the documentation generated.
cd $ORIGINAL_CWD;
mkdir projects

## Copy the generated documentation to the
## target diretory.
cd ./repos
for DIR in $(ls); do
    echo $DIR;
    if [ -e $DIR/doxygen ]; then
        cp --parents -rf $DIR/doxygen ../projects/
    fi;
done;


## Clean up the target dir and copy everything
## that was build to there.
cd $ORIGINAL_CWD;

rm -rf $TARGET_DIR;
mkdir -p $TARGET_DIR;
cp -rf index.html $TARGET_DIR;
cp -rf projects   $TARGET_DIR;
