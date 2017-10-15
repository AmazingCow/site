#!/usr/bin/python
#coding=utf-8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        download_repos.py                         ##
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

################################################################################
## Imports                                                                    ##
################################################################################
import os;
import os.path;
import urllib;
import json;

################################################################################
## Constants                                                                  ##
################################################################################
BASE_URL  = "https://api.github.com/users/{ORGANIZATION_NAME}/repos"
BASE_PATH = "amazingcow_repos"

ORGANIZATION_NAMES = [
    "AmazingCow-Game-Core",
    "AmazingCow-Game-Framework",
    "AmazingCow-Game-Tool",
    "AmazingCow-Game",
    "AmazingCow-Libs",
    "AmazingCow-Tools",
    "AmazingCow-Imidiar",
];


################################################################################
## Helper Functions                                                           ##
################################################################################
def make_dir(name):
    fullname = os.path.join(BASE_PATH, name);
    if(os.path.isdir(fullname) == False):
        print "Creating directory: ({0})".format(fullname);
        os.system("mkdir -p {0}".format(fullname));

    return fullname;


def fetch_list_repos(organization_name):
    url      = BASE_URL.format(ORGANIZATION_NAME=organization_name);
    response = urllib.urlopen(url);
    data     = json.loads(response.read());


    print "Fetching repos for: ({0})".format(organization_name);
    repos = [];
    for info in data:
        repos.append(
            {
                "url"  : info["clone_url"],
                "name" : info["name"     ]
            }
        );

    print "\tDone. Found ({0}) repos...".format(len(repos));
    return repos;


def clone_repos(repos_info, repos_dir):
    for repo_info in repos_info:
        print "Clonning repo ({0}) in ({1})".format(
            repo_info["name"],
            repos_dir
        );

        repo_full_dir = os.path.join(repos_dir, repo_info["name"]);

        if(os.path.isdir(repo_full_dir)):
            print "\tRepo ({0}) already cloned...".format(repo_info["name"]);
            continue;

        ## Commands...                # Supress output...
        mkdir    = "mkdir -p  {0}   > /dev/null 2>&1".format(repo_full_dir);
        cd       = "cd        {0}   > /dev/null 2>&1".format(repo_full_dir);
        clone    = "git clone {0} . > /dev/null 2>&1".format(repo_info["url"]);

        full_cmd = "{0} && {1} && {2}".format(
            mkdir,
            cd,
            clone,
        );
        os.system(full_cmd);

################################################################################
## Script                                                                     ##
################################################################################
for organization_name in ORGANIZATION_NAMES:
     repos_dir  = make_dir(organization_name);
     repos_info = fetch_list_repos(organization_name);
     clone_repos(repos_info, repos_dir);

     print "----\n"

