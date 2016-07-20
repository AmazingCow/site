#!/bin/bash

## Vars
TARGET_DIR=$1;
if [ -z "$TARGET_DIR" ]; then
    TARGET_DIR="./build";
fi;

ORIGINAL_CWD=$(pwd);
OUTPUT_DIR=$TARGET_DIR/~n2omatt;

## Update the Certifications repo
cd $ORIGINAL_CWD
cd ./_build_stuff/MyCerts;
git pull origin master

## Generate the Certifications
cd $ORIGINAL_CWD
cd ./_build_stuff/certification_scripts;
./generate_certifications.sh;


## Create the output dir
cd $ORIGINAL_CWD;
rm -rf $OUTPUT_DIR;
mkdir -p $OUTPUT_DIR;

## Copy the stuff...
cp index.html   $OUTPUT_DIR
cp -rf resume   $OUTPUT_DIR
cp -rf img      $OUTPUT_DIR
cp -rf certs    $OUTPUT_DIR
cp -rf lectures $OUTPUT_DIR
