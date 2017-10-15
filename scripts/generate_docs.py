#!/usr/bin/python
##~---------------------------------------------------------------------------##
##                     _______  _______  _______  _     _                     ##
##                    |   _   ||       ||       || | _ | |                    ##
##                    |  |_|  ||       ||   _   || || || |                    ##
##                    |       ||       ||  | |  ||       |                    ##
##                    |       ||      _||  |_|  ||       |                    ##
##                    |   _   ||     |_ |       ||   _   |                    ##
##                    |__| |__||_______||_______||__| |__|                    ##
##                             www.amazingcow.com                             ##
##  File      : generate_docs.py                                              ##
##  Project   : site                                                          ##
##  Date      : Oct 15, 2017                                                  ##
##  License   : GPLv3                                                         ##
##  Author    : n2omatt <n2omatt@amazingcow.com>                              ##
##  Copyright : AmazingCow - 2017                                             ##
##                                                                            ##
##  Description :                                                             ##
##---------------------------------------------------------------------------~##

################################################################################
## Imports                                                                    ##
################################################################################
import sys;
import os.path;

################################################################################
## Constants                                                                  ##
################################################################################
kPathScript = os.path.realpath(__file__);
kDirScript  = os.path.dirname(kPathScript);
kDirBase    = os.path.abspath(os.path.join(kDirScript, "../"));
kDirRepos   = os.path.abspath(os.path.join(kDirBase, "repos"));
kDirDocs    = os.path.abspath(os.path.join(kDirBase, "_output/docs"));

################################################################################
## Script                                                                     ##
################################################################################
os.system("rm -rf   {docs_dir}".format(docs_dir = kDirDocs));
os.system("mkdir -p {docs_dir}".format(docs_dir = kDirDocs));

for dir in os.listdir(kDirRepos):
    fullpath = os.path.join(kDirRepos, dir);
    os.chdir(fullpath);

    if(not os.path.exists("Doxyfile")):
        continue;

    ## Generate the docs.
    os.system("doxygen > /dev/null 2>&1");

    ## Copy the generate files to output folder.
    sys.stderr.write("#Generating docs for: ({0})\n".format(dir));
    os.system("mkdir -p {dir}".format(dir=dir));
    os.system("cp -R {repo_docs_dir} {docs_dir}".format(
        repo_docs_dir = os.path.join(fullpath, "doxygen"),
        docs_dir      = os.path.join(kDirDocs, dir)
    ));

    ## Append project to list.
    print("{item} , {content}, {url}".format(
        item    = "",
        content = dir,
        url     = os.path.join("./docs", dir)
    ));

    os.chdir(kDirRepos);
