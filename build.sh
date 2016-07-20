#!/bin/bash

## Vars
TARGET_DIR=$1;
if [ -z "$TARGET_DIR" ]; then
    TARGET_DIR="./build";
fi;

ORIGINAL_CWD=$(pwd);
TARGET_DIR=$(readlink -f $TARGET_DIR);
TEMP_DIR=$(readlink -f ./temp);

## Download the repositories if needed.
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


# ## Clean up the target dir
cd $ORIGINAL_CWD;
rm -rf   $TEMP_DIR;
mkdir -p $TEMP_DIR;


## Create the ~n2omatt stuff.
cd \~n2omatt
./build.sh $TEMP_DIR


## Copy everything that was build to there.
cd $ORIGINAL_CWD;
cp -rf index.html $TEMP_DIR;
cp -rf projects   $TEMP_DIR;


rm -rf $TARGET_DIR
mv $TEMP_DIR $TARGET_DIR
