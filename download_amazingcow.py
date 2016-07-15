#!/usr/bin/python

## Imports ##
import os;
import os.path;
import urllib;
import json;

#Sometimes I don't have termcolor.
try:
    from termcolor import colored;
except ImportError, e:
    def colored(msg, color):
        return msg;


## Paths.
BASE_URL  = "https://api.github.com/users/{ORGANIZATION_NAME}/repos"
BASE_PATH = os.path.expanduser(".");


ORGANIZATION_NAMES = [
    "AmazingCow-Game-Core",
    "AmazingCow-Game-Framework",
    "AmazingCow-Game-Tool",
    "AmazingCow-Game",
    "AmazingCow-Libs",
    "AmazingCow-Tools",
];


def fetch_list_repos(organization_name):
    url      = BASE_URL.format(ORGANIZATION_NAME=organization_name);
    response = urllib.urlopen(url);
    data     = json.loads(response.read());


    print "Fetching repos for: ({0})".format(organization_name);
    repos = [];
    for info in data:
        repos.append(
            { "url"  : info["clone_url"],
              "name" : info["name"].lower()
            });

    return repos;


def clone_repos(repos_info, repos_dir):
    for repo_info in repos_info:
        repo_full_dir = os.path.join(repos_dir, repo_info["name"]);

        if(os.path.isdir(repo_full_dir)):
            print "Repo already cloned... Updating..";
            os.system("cd {0} && git pull --all".format(repo_full_dir));
        else:
            print "Clonning repo ({0}) in ({1})".format(repo_info["name"], repos_dir);
            os.system("git clone {0} {1}".format(repo_info["url"], repo_full_dir));


for organization_name in ORGANIZATION_NAMES:
     repos_info = fetch_list_repos(organization_name);
     clone_repos(repos_info, "./repos");

     print "----"
