#!/bin/bash


################################################################################
## Pre-script stuff...                                                        ##
################################################################################
## Clean up stuff...
rm    -rf _output;
mkdir -p  _output;

# ## Repos are needed for other stuff...
./scripts/download_repos.py;
./scripts/update_repos.py;

################################################################################
## Index page.                                                                ##
################################################################################
./scripts/build_index.py ./templates/index/index.template > _output/index.html;

################################################################################
## Docs                                                                       ##
################################################################################
mkdir -p _output/docs;
./scripts/generate_docs.py > ./templates/docs/docs.list;
./scripts/build_index.py ./templates/docs/index.template > _output/docs/index.html;

################################################################################
## Floss                                                                      ##
################################################################################
mkdir -p _output/floss;
./scripts/build_index.py ./templates/floss/index.template > _output/floss/index.html;

################################################################################
## Contact                                                                    ##
################################################################################
mkdir -p _output/contact;
./scripts/build_index.py ./templates/contact/index.template > _output/contact/index.html;


################################################################################
## Images                                                                     ##
################################################################################
cp -R img _output/img


################################################################################
## Copy                                                                       ##
################################################################################
rsync -a  ./_output/* /var/www/html/