##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        create_projects_info.sh                   ##
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

echo "--> Creating projects info...";

BASE_DIR="amazingcow_repos";
INTERMEDIATE_DIR="intermediate/projects_info"

## Clean up the projects_info_folder
rm -rfv   "$INTERMEDIATE_DIR";
mkdir -pv "$INTERMEDIATE_DIR";

## Generate info for all AmazingCow orgs.
for ORG_NAME in $(ls $BASE_DIR); do
    ORG_DIR=$BASE_DIR/$ORG_NAME;

    ## Generate info for all repos within organization.
    for PROJECT_NAME in $(ls $ORG_DIR); do
        PROJECT_DIR="$ORG_DIR/$PROJECT_NAME";


        ## The Repository info is inside a branch called
        ## "site_info", so we need:
        ##   1 - Checkout to site_info branch
        ##   2 - Update the branch (maybe we updated something...)
        ##   3 - Call script to process the info file.
        ##   4 - Go back to master.
        ## That's all...
        cd "$PROJECT_DIR";

        echo "($PROJECT_NAME) - Creating info...";
        ## (1) Check if we have on site_info branch already.
        ##     If so, just checkout, otherwise create a branch...
        BRANCH_COUNT=$(git branch -a | grep  "site_info" | wc -l);
        if [ $BRANCH_COUNT == 2 ]; then
            echo -e "\t  Already have site_info branch...";
            git checkout site_info > /dev/null 2>&1;
        else
            echo -e "\t  DON'T HAVE have site_info branch...";
            git checkout --track -b site_info origin/site_info > /dev/null 2>&1;
        fi;

        ## (2) Update the branch...
        git pull origin site_info  2>&1;
        cd - > /dev/null

        ## (3) Process the info.
        ./process_project_info.py "$PROJECT_DIR/site_info/info"

        ## (4) Go back to master
        cd "$PROJECT_DIR";
        git checkout master > /dev/null 2>&1
        cd - > /dev/null
    done;
done;
