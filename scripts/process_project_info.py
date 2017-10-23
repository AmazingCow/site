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
##  File      : process_project_info.py                                       ##
##  Project   : site                                                          ##
##  Date      : Oct 15, 2017                                                  ##
##  License   : GPLv3                                                         ##
##  Author    : n2omatt <n2omatt@amazingcow.com>                              ##
##  Copyright : AmazingCow - 2017                                             ##
##                                                                            ##
##  Description :                                                             ##
##                                                                            ##
##---------------------------------------------------------------------------~##

################################################################################
## Imports                                                                    ##
################################################################################
import os;
import os.path;
import sys;
from pprint import pprint;

## Our info file looks like this.
## I think that the sections are straightforward to understand,
## the only one that needs further explanation is the "Section".
##
## The "Section" section is the place that the project will be
## put on the site. So if a project is a Game we indicate there
## so in the index.html it will be placed on Games section.
##
## Title:
##     CoreClock
## Description:
##     Small library intended to easy the time tracking in games.
## URL:
##     Github, http://github.com/AmazingCow-Game-Core/CoreClock
##     Docs, docs.amazingcow.com/coreclock
## Owner:
##     AmazingCow Labs
## Section:
##     Game Core

################################################################################
## Constants                                                                  ##
################################################################################
kPathScript = os.path.realpath(__file__);
kDirScript  = os.path.dirname(kPathScript);
kDirBase    = os.path.abspath(os.path.join(kDirScript, "../"));
kDirRepos   = os.path.abspath(os.path.join(kDirBase, "repos"));


kTags = ["Title:", "Description:", "URL:", "Owner:", "Section:"];

kHTML_Fmt = """
<li>
    <b>{title}:</b> ({urls})
    <br>
    {desc}
</li>
<hr>
""";


################################################################################
## Variables                                                                  ##
################################################################################



################################################################################
## Functions                                                                  ##
################################################################################
def read_info(lines, index):
    result = [];
    while(index < len(lines)):
        line = lines[index].replace("\n", "").strip();
        if(line not in kTags):
            result.append(line);
        else:
            break

        index += 1;

    return result;

def process_info(info_file):
    info  = {};
    lines = open(info_file).readlines()

    for i in range(len(lines)):
        line = lines[i].replace("\n", "").strip();
        if(line in kTags):
            info[line] = read_info(lines, i + 1);
            i += len(info[line]);

    info["Title:"       ] = "".join(info["Title:"      ]);
    info["Description:" ] = "".join(info["Description:"]);
    info["Owner:"       ] = "".join(info["Owner:"      ]);
    info["Section:"     ] = "".join(info["Section:"    ]);

    return info;


def make_html_urls(urls):
    r = "";
    for i in xrange(0, len(urls)):
        url_info = urls[i];

        name, url = url_info.split(",");
        r += "<a href=\"{0}\">{1}</a>".format(url,name);

        if(i + 1 < len(urls)):
            r += " - ";

    return r;


def make_html(sections_dict):
    html = "";
    for key in sorted(sections_dict.keys()):
        html += "<b>{0}</b> ({1} project{2})".format(
            key,
            len(sections_dict[key]),
            "s" if len(sections_dict[key]) > 1 else ""
        );
        html += "<ul>"
        for info in sections_dict[key]:
            html += kHTML_Fmt.format(
                title = info["Title:"],
                urls  = make_html_urls(info["URL:"]),
                desc  = info["Description:"]
            );
        html += "</ul>"
    return html;




################################################################################
## Script                                                                    ##
################################################################################
def main():
    sections_dict = {};
    for dir in os.listdir(kDirRepos):
        dir_fullpath  = os.path.join(kDirRepos, dir);
        info_fullpath = os.path.join(dir_fullpath, "docs/site_info");

        if(not os.path.exists(info_fullpath)):
            continue;

        info         = process_info(info_fullpath);
        info_section = info["Section:"];
        if(info_section not in sections_dict.keys()):
            sections_dict[info_section] = [];

        sections_dict[info_section].append(info);

    print make_html(sections_dict);

if __name__ == '__main__':
    main();
