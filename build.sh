#!/bin/bash

## SOME CONSTANTS ##
COLOR_CREATING_DIRECTORY_TREE="\033[031m"
COLOR_LOCAL_BUILDING="\033[032m"
COLOR_MD_PROCESSING="\033[033m"
COLOR_FILE_COPYING="\033[035m"
COLOR_RESET="\033[0m"

## SOME VARS ##
SRC_DIR=./src
SNIPPETS="./scripts/insert_snippets.py ./snippets"

BUILD_DIR=$1
BUILD_TEMP_DIR=temp
TEMP_FILE="temp_file.txt"
BUILD_DATE=$(date --utc);
BUILD_NUMBER=""

if [ -z "$1" ]; then
    echo "Missing build folder";
    exit 1;
fi;

# Clean up the build folder.
rm -rf $BUILD_TEMP_DIR


start_create_dir_tree()
{
    echo -en ${COLOR_CREATING_DIRECTORY_TREE};
    echo "--------> BEGIN Creating directory tree. <--------";

    NUMBER_OF_DIRS="0";
    find $SRC_DIR -type d -not -path '*/\.*' >  $TEMP_FILE;

    while read LINE; do
        DIR_PATH=$(echo $LINE | replace $SRC_DIR $BUILD_TEMP_DIR);
        mkdir -p "$DIR_PATH";
        NUMBER_OF_DIRS=$(( $NUMBER_OF_DIRS + 1));

        echo "Build dir path: $DIR_PATH";
    done < $TEMP_FILE #Creating directory tree

    echo "Builded $NUMBER_OF_DIRS directories.";
    echo "--------> END Creating directory tree. <--------";
}

start_local_build()
{
    echo -en $COLOR_LOCAL_BUILDING;
    echo "--------> BEGIN Local Building. <--------";

    find $SRC_DIR -type f -not -path '*/\.*' -iname "_*.sh" >  $TEMP_FILE;
    NUMBER_OF_BUILDS="0";

    while read LINE; do
        CURRENT_DIR=$(dirname $LINE);
        CURRENT_FILE=$(basename $LINE);

        ## File is local build - Run it.
        if [ "$CURRENT_FILE" == "_build.sh" ]; then
            OLDCWD=$(pwd)

            cd $CURRENT_DIR;
            ./$CURRENT_FILE >/dev/null 2>&1
            cd $OLDCWD;

            NUMBER_OF_BUILDS=$(( $NUMBER_OF_BUILDS + 1 ));

            echo "Start build of: $CURRENT_DIR/$CURRENT_FILE";
        fi;

    done < $TEMP_FILE #Local building

    echo "Peformed  $NUMBER_OF_BUILDS builds";
    echo "--------> END Local Building. <--------";
}

start_md_processing()
{
    echo -en $COLOR_MD_PROCESSING;
    echo "MD Processing.----------------------------------------------------------"
    find $SRC_DIR -type f -not -path '*/\.*' -iname "_*.md" >  $TEMP_FILE;
    while read LINE; do
        CURRENT_DIR=$(dirname $LINE);
        CURRENT_FILE=$(basename $LINE);

        TARGET_DIR=$(echo $CURRENT_DIR   | replace $SRC_DIR $BUILD_TEMP_DIR);
        TARGET_FILE=$(echo $CURRENT_FILE | sed s/md/html/g | sed s/_//g);

        echo "Dir   : $CURRENT_DIR";
        echo "File  : $CURRENT_FILE";
        echo "TDir  : $TARGET_DIR";
        echo "TFile : $TARGET_FILE";
        echo "Final : $TARGET_DIR/$TARGET_FILE";

        mkdir -p $TARGET_DIR;
        echo "<!-- Build $BUILD_NUMBER - Date $BUILD_DATE -->" > $TARGET_DIR/$TARGET_FILE
        cat $CURRENT_DIR/$CURRENT_FILE | $SNIPPETS | $AMAZINGCOW_ENV_MARKDOWN >> $TARGET_DIR/$TARGET_FILE;

    done < $TEMP_FILE #MD Processing.
}

start_file_copy()
{
    echo -en $COLOR_FILE_COPYING;
    echo "File Copying.-----------------------------------------------------------"

    find $SRC_DIR -type f -not -path '*/\.*'  -not -iname "_*.md" >  $TEMP_FILE;
    FILES_TO_COPY=$(cat $TEMP_FILE | wc -l);

    while read LINE; do
        CURRENT_DIR=$(dirname $LINE);
        CURRENT_FILE=$(basename $LINE);
        CURRENT_EXT=$(echo $CURRENT_FILE | cut -d. -f2);

        TARGET_DIR=$(echo $CURRENT_DIR   | replace $SRC_DIR $BUILD_TEMP_DIR);
        TARGET_FILE=$(echo $CURRENT_FILE | sed s/md/html/g);

        echo "$FILES_TO_COPY files remaining...";
        FILES_TO_COPY=$(( FILES_TO_COPY -1 ));

        mkdir -p $TARGET_DIR;
        cat $CURRENT_DIR/$CURRENT_FILE > $TARGET_DIR/$TARGET_FILE;

    done < $TEMP_FILE #File Copying.
}


move_build_temp()
{
    rm -rf $BUILD_DIR;
    mkdir -p $BUILD_DIR;

    mv $BUILD_TEMP_DIR/* $BUILD_DIR
    rm -rf $BUILD_TEMP_DIR;
}

update_build_number()
{
    echo "--------> BEGIN Update the Build Number <--------";

    number=$(cat buildnumber.txt);
    BUILD_NUMBER=$(( $number + 1 ));

    echo $BUILD_NUMBER > buildnumber.txt

    echo "Build number was: $number";
    echo "Build number is : $BUILD_NUMBER";

    echo "--------> END Update the Build Number <--------";
}

commit_build()
{
   git add .;
   git commit -m "Build $BUILD_NUMBER - Date $BUILD_DATE";
}

update_build_number
start_create_dir_tree
start_local_build
# start_md_processing
# start_file_copy
# move_build_temp
# commit_build

echo -en $COLOR_RESET;


echo "done..."
