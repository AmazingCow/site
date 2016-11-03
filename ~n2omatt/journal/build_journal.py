#!/usr/bin/python
################################################################################
## file   : build_journal.py                                                  ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
################################################################################

################################################################################
## Imports                                                                    ##
################################################################################
import json;
import os;
import time;
import os.path;

buffer = [];

def log_print(s):
    pass;
    # print s;

def buf_print(s):
    log_print(s);
    global buffer;
    buffer.append(s);


def get_date_from_filename(filename):
    basename = os.path.basename(filename);
    return time.strptime(basename.replace(".json", ""), "%b_%d_%Y")

def sort_files_by_filename_date(files_list):
    tm_list = [];
    for filename in files_list:
        tm_list.append(
            get_date_from_filename(filename)
        );

    tm_list.sort(reverse=True);

    files_list = [];
    for tm in tm_list:
        files_list.append(
            str.lower(time.strftime("%b_%d_%Y", tm) + ".json")
        );

    return files_list;



def get_header_tag(tm):
    return "<h3>%s</h3>" %(time.strftime("%b %d, %Y", tm));

def get_start_action_tag(type, name):
    return "<b>%s - %s</b>" %(type.capitalize(), name)

def get_start_list_tag():
    return "<ul>";

def get_end_list_tag():
    return "</ul>";

def get_start_item_tag():
    return "<li>";

def get_end_item_tag():
    return "</li>";

def get_hyperlink_tag(name, url):
    return "<a href=\"%s\">%s</a>" %(url, name);


def process_action_watched(obj):
    buf_print(get_start_item_tag());

    buf_print(get_hyperlink_tag(obj.keys()[0], obj[obj.keys()[0]]));

    buf_print(get_end_item_tag());

def process_action_read(obj):
    buf_print(get_start_item_tag());

    s = obj["title"] + " - " + obj["pages"];
    buf_print(s);

    buf_print(get_end_item_tag());


def process_action(action_type, action_obj):
    action_type = action_type.lower();
    if(action_type == "watched"):
        for a in action_obj:
            process_action_watched(a);
    if(action_type == "read"):
        for a in action_obj:
            process_action_read(a);


def process_file(filename):
    log_print("Processing file: " + filename);
    json_obj = json.load(file(filename));

    date = get_date_from_filename(filename);
    buf_print(get_header_tag(date));
    buf_print(get_start_list_tag());

    for key in sorted(json_obj.keys()):
        action_type = key.split("-")[0];
        action_name = key.split("-")[1];

        buf_print(get_start_action_tag(action_type, action_name));
        process_action(action_type, json_obj[key]);

    buf_print(get_end_list_tag());


files_list = sort_files_by_filename_date(os.listdir("./data"));
for filename in files_list:
    process_file(os.path.join("./data", filename));

for l in buffer:
    print(l.encode("utf-8"));
