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
##  File      : download_repos.py                                             ##
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

kDirBase = os.path.abspath(os.path.join(kDirScript, "../"));

kDirLib              = os.path.abspath(os.path.join(kDirBase, "lib"));
kDirLibDownloadRepos = os.path.abspath(os.path.join(kDirLib, "DownloadRepos"));

kDirRepos = os.path.abspath(os.path.join(kDirBase, "repos"));


################################################################################
## Script                                                                     ##
################################################################################
orgs=[
    "AmazingCow-Game-Core",
    "AmazingCow-Game-Framework",
    "AmazingCow-Game-Tool",
    "AmazingCow-Game",
    "AmazingCow-Libs",
    "AmazingCow-Tools",
    "AmazingCow-Imidiar",
    "AmazingCow-Services",
    "AmazingCow",
];

for org in orgs:
    ## Call the Repo Fetcher.
    repo_fetcher = os.path.join(kDirLibDownloadRepos, "github_repo_fetcher.py");
    repos_list   = os.path.join(kDirScript, org + ".list");

    os.system("{script} --org={org} --output={repos_list}".format(
        script     = repo_fetcher,
        org        = org,
        repos_list = repos_list
    ));

    ## Call the Repo Downloader.
    repo_downloader = os.path.join(kDirLibDownloadRepos, "download_repos.py");
    os.system("{script} --org=AmazingCow --base-path={base_path} --repos-list={repos_list}".format(
        script     = repo_downloader,
        base_path  = kDirRepos,
        repos_list = repos_list
    ));

    ## Clean up the temp files...
    os.system("rm {repos_list}".format(repos_list=repos_list));
