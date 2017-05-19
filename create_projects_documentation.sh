#!/bin/bash
echo "--> Creating projects documentation...";

OUT_DIR="_Output/docs";
BASE_DIR="amazingcow_repos";

## Create the output directory...
mkdir -p "$OUT_DIR"

## Generate the documentation for all the AmazingCow Organizations.
for ORG_NAME in $(ls $BASE_DIR); do
    ORG_DIR=$BASE_DIR/$ORG_NAME;

    ## Generate the documentation of all repos within the organizatin.
    for PROJECT_NAME in $(ls $ORG_DIR); do

        SRC_DIR=$ORG_DIR/$PROJECT_NAME;
        DST_DIR=$OUT_DIR/$PROJECT_NAME;

        ## Here is where the actual work happens...
        cd $SRC_DIR

        if [ -e "Doxyfile" ]; then
            echo -e "($PROJECT_NAME) - There is a Doxyfile";
            echo -e "\tGenerating documentation...";
            doxygen > /dev/null 2>&1;
            echo -e "\tDone...";
        else
            echo -e "($PROJECT_NAME) doesn't have Doxyfile.";
            echo -e "\tSkipping...";
        fi;

        cd - > /dev/null;

        ## Copy the generated documentation to output folder.
        if [ -e "$SRC_DIR/doxygen" ]; then
            echo -e "Copying documentation for ($PROJECT_NAME)...";
            cp -r $SRC_DIR/doxygen $DST_DIR/doxygen
            echo -e "\tDone..."
        fi;
    done;
done;
