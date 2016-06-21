#!/usr/bin/python

import os;
import os.path;
import sys;
import re;

snippets_dir = sys.argv[1];
# src_lines = open(sys.argv[1]).readlines();
i = 0;

while(True):
    try:
        line = sys.stdin.next();
    except:
        exit(0);

    line = line.replace("\n", "");
    if(re.search("\{\!.*\!\}", line)):
        snippet_name = line.replace("{!", "").replace("!}", "").replace("<p>", "").replace("</p>", "");
        snippet_path = os.path.join(snippets_dir, snippet_name);
        snippet_lines = open(snippet_path).readlines();
        for line in snippet_lines:
            print line,
    else:
        print line;
    i += 1;

