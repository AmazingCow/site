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
##  File      : build_template_list.py                                        ##
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
## Scripts                                                                    ##
################################################################################
filename = sys.argv[1];
lines    = open(filename).readlines();

print "<b>{title}</b><br>".format(
    title=os.path.basename(filename).replace(".list", "").capitalize()
);

print "<ul>";
for line in lines:
    if(len(line.replace("\n", "")) == 0):
        continue;

    item, content, url = line.split(",");
    print "<li>{item} <a href=\"{url}\">{content}</a></li>".format(
        item   = item   .replace("\n", "").strip(" "),
        content= content.replace("\n", "").strip(" "),
        url    = url    .replace("\n", "").strip(" ")
    );

print "</ul>";
