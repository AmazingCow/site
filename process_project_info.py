#!/usr/bin/python
#coding=utf-8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        process_project_info.py                   ##
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
import sys;

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
kTags = ["Title:", "Description:", "URL:", "Owner:", "Section:"];

kHTML_Fmt = """
<li>
    <b>{title}:</b> ({urls})
    <br>
    {desc}
</li>
<hr>
""";

kOutputPath = "intermediate/projects_info";

################################################################################
## Variables                                                                  ##
################################################################################
result    = "";
info_dict = {};
curr_key  = None;

################################################################################
## Functions                                                                  ##
################################################################################
def make_urls_from_info(urls_list):
    r = "";
    for i in xrange(0, len(urls_list)):
        url_info = urls_list[i];

        splited = url_info.split(",");
        url     = splited[1];
        name    = splited[0];

        r += "<a href=\"{0}\">{1}</a>".format(
            url,
            name
        );

        if(i + 1 < len(urls_list)):
            r += " - ";

    return r;


################################################################################
## Script                                                                    ##
################################################################################
def main(filename):
    in_file  = open(filename);

    print "---> Processing Project Info for: ({0})".format(filename);

    for line in in_file.readlines():
        line = line.lstrip(" ").replace("\n", "");

        if(line == ""):
            continue;

        if(line in kTags):
            curr_key            = line;
            info_dict[curr_key] = [];
            continue;

        info_dict[curr_key].append(line);


    html = kHTML_Fmt.format(
        title = "".join(info_dict["Title:"]                   ),
        urls  = "".join(make_urls_from_info(info_dict["URL:"])),
        desc  = "".join(info_dict["Description:"]             )
    );

    section_name = "".join(info_dict["Section:"]);
    fullpath     = os.path.join(kOutputPath, section_name);

    out_file = open(fullpath, "a");
    out_file.write(html);

    out_file.close();
    in_file.close ();


if __name__ == '__main__':
    filename = sys.argv[1];
    try:
        main(filename);
    except Exception as e:
        print filename;
        print e;

        import pdb;
        pdb.set_trace();

