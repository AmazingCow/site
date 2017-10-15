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
##  File      : update_repos.py                                               ##
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

################################################################################
## Script                                                                     ##
################################################################################
for dir in os.listdir(kDirRepos):
    fullpath = os.path.join(kDirRepos, dir);
    os.system("cd {path} && git reset --hard master && git pull origin master".format(
        path=fullpath
    ));
