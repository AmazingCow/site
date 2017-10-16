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
##  File      : build_index.py                                                ##
##  Project   : site                                                          ##
##  Date      : Oct 14, 2017                                                  ##
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
import subprocess;

################################################################################
## Constants                                                                  ##
################################################################################
kPathScript   = os.path.realpath(__file__);
kDirScript    = os.path.dirname(kPathScript);
kDirTemplates = os.path.abspath(os.path.join(kPathScript, "../../templates"));


################################################################################
## Functions                                                                  ##
################################################################################
## Function bellow is taken from:
##     http://blog.endpoint.com/2015/01/getting-realtime-output-using-python.html
def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE);
    result  = "";
    while(True):
        output = process.stdout.readline()
        if(output == '' and process.poll() is not None):
            break
        if(output):
            result += output.strip() + "\n";

    rc = process.poll();
    return result;


def run_template(line):
    ## Isolate the template declaration from line.
    start_index = line.find("__TEMPLATE_");
    end_index   = line.find(" ", start_index,);
    template    = line[start_index: end_index];

    ## Get which template it's.
    action, content = filter(
        None,
        template.replace("__TEMPLATE", "").lower().replace("_", " ").split(" ")
    );


    if(action == "list"):
        return line[0:start_index] + build_template_list(content) + line[end_index:];

    if(action == "process"):
        return build_process_projects();

    return "";


def build_template_list(list_name):
    filename   = os.path.join(kDirTemplates, list_name) + ".list";
    scriptname = os.path.join(kDirScript, "build_template_list.py");

    return run_command("{script} {filename}".format(
        script   = scriptname,
        filename = filename
    ));


def build_process_projects():
    scriptname = os.path.join(kDirScript, "process_project_info.py");

    return run_command("{script}".format(
        script = scriptname,
    ));


################################################################################
## Script                                                                     ##
################################################################################
filename = sys.argv[1];
lines    = open(filename).readlines();

for line in lines:
    line = line.replace("\n", "");
    if("__TEMPLATE" in line):
        line = run_template(line);

    print line;
