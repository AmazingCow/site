#!/bin/bash
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        build.sh                                  ##
##            █ █        █ █        site                                      ##
##             ████████████                                                   ##
##           █              █       Copyright (c) 2017                        ##
##          █     █    █     █      AmazingCow - www.AmazingCow.com           ##
##          █     █    █     █                                                ##
##           █              █       N2OMatt - n2omatt@amazingcow.com          ##
##             ████████████         www.amazingcow.com/n2omatt                ##
##                                                                            ##
##                  This software is licensed as GPLv3                        ##
##                 CHECK THE COPYING FILE TO MORE DETAILS                     ##
##                                                                            ##
##    Permission is granted to anyone to use this software for any purpose,   ##
##   including commercial applications, and to alter it and redistribute it   ##
##               freely, subject to the following restrictions:               ##
##                                                                            ##
##     0. You **CANNOT** change the type of the license.                      ##
##     1. The origin of this software must not be misrepresented;             ##
##        you must not claim that you wrote the original software.            ##
##     2. If you use this software in a product, an acknowledgment in the     ##
##        product IS HIGHLY APPRECIATED, both in source and binary forms.     ##
##        (See opensource.AmazingCow.com/acknowledgment.html for details).    ##
##        If you will not acknowledge, just send us a email. We'll be         ##
##        *VERY* happy to see our work being used by other people. :)         ##
##        The email is: acknowledgment_opensource@AmazingCow.com              ##
##     3. Altered source versions must be plainly marked as such,             ##
##        and must not be misrepresented as being the original software.      ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
##----------------------------------------------------------------------------##

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

