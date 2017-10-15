#!/usr/bin/python
#coding=utf-8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        replace_index_template.py                 ##
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
import sys;
import os;
import os.path;


################################################################################
## Constants                                                                  ##
################################################################################
kProjectsInfo_Path = "intermediate/projects_info";


################################################################################
## Functions                                                                  ##
################################################################################
def read_file_text(filename):
    entry_file = open(filename);
    all_lines  = entry_file.readlines();

    entry_file.close();

    return "".join(all_lines);

def write_file_text(blog_entry_fullpath, text):
    outfile  = open(blog_entry_fullpath, "w");

    outfile.write(text);
    outfile.close();


def generate_html_for_category(category):
    fullpath      = os.path.join(kProjectsInfo_Path, category);
    projects_text = read_file_text(fullpath);
    count         = len(projects_text.split("<li>")) -1;
    category_url  = category.replace(" ", "-");

    ## THIS IS NASTY:
    if(category_url == "Game-Tools"):
        category_url = "Game-Tool";

    html_fmt = """
    <p>
        <b>{category_name}</b>
            (<a href=\"http://github.com/AmazingCow-{category_url}\">Github</a>)
            - {projects_count} projects
        <br/>
    </p>
    <ul>
        {projects_list}
    </ul>
    """;

    return html_fmt.format(
        category_name  = category,
        category_url   = category_url,
        projects_count = count,
        projects_list  = projects_text
    );



################################################################################
## Script                                                                     ##
################################################################################
def main():
    print "--> Replacing index template...";

    html_contents = "";
    for category in sorted(os.listdir(kProjectsInfo_Path)):
        html_contents += generate_html_for_category(category);

    index_template = read_file_text("index.template");
    index_replaced = index_template.replace(
        "__TEMPLATE_REPLACE_PROJECTS__",
        html_contents
    );

    write_file_text("_Output/index.html", index_replaced);

if __name__ == '__main__':
    main()
