#!/bin/bash

SCRIPT=$(realpath -s $0);
SCRIPTPATH=$(dirname $SCRIPT);

cd $SCRIPTPATH;
git pull origin master;

./build_site.sh 
