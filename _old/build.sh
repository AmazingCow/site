#!/bin/bash

DESTINATION_DIR="../public_html"
if [ -n "$1" ]; then
    DESTINATION_DIR="$1";
fi;

################################################################################
## Clean everything at start                                                  ##
################################################################################
echo "--> Cleaning Output folder...";
rm    -vrf "_Output";
mkdir -vp  "_Output";


################################################################################
## Build the stuff...                                                         ##
################################################################################
./update_repositories.sh
./create_projects_directories.sh
./create_projects_documentation.sh
./create_projects_info.sh
./replace_index_template.py
./copy_images.sh

## Notice to n2omatt May 26, 2017 - IDOT!
## For some IDIOTIC reasons I fucked up the paths...
## So the projects site_info expects that the documentation to be in:
##      docs.amazingcow.com/projectname <-- NOTICE THE LOWER CASE.
## But the READMEs want the documentation in:
##      amazingcow.com/projects/ProjectName/doxygen
## I'm so dumb... but I wont change a 100^100 projects READMEs or site_info
## stuff, so here as HACK from hell...
## I really sorry about that, but I got tired of try to make this fucking site
## works as I want...
CWD=$(pwd);
cd ./_Output/docs;

for DOC_DIRECTORY in $(ls .); do
    ## This resolves that case problem...
    LOWERCASE_DIRECTORY=$(echo $DOC_DIRECTORY | tr [:upper:] [:lower:]);
    if [ "$DOC_DIRECTORY" != "$LOWERCASE_DIRECTORY" ]; then
        mv $DOC_DIRECTORY $LOWERCASE_DIRECTORY;
    fi;

    ## This resolves the README paths.
    mkdir -vp ../projects/$LOWERCASE_DIRECTORY;
    ln -sv --relative $LOWERCASE_DIRECTORY ../projects/$LOWERCASE_DIRECTORY/doxygen
done;
cd - > /dev/null

################################################################################
## Copy to destination folder                                                 ##
################################################################################
rm -rfv $DESTINATION_DIR/docs
rm -rfv $DESTINATION_DIR/img
rm -rfv $DESTINATION_DIR/index.html
rm -rfv $DESTINATION_DIR/projects

cp -rv _Output/* $DESTINATION_DIR/

