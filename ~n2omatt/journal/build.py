#!/usr/bin/python
################################################################################
## file   : build.py                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
## Create the journal page and copy it to Output folder.                      ##
################################################################################


################################################################################
## Imports                                                                    ##
################################################################################
import os;


################################################################################
## Script                                                                     ##
################################################################################
## Clean up.
os.system("rm -rf Output");
os.system("mkdir Output");

## Create the Journal actions into a separated file
##   We gonna merge the hand written page with the
##   machine generated next.
os.system("./build_journal.py > journal.tmp");

## Read the contents of the files.
original_lines = open("index_original.html").readlines();
journal_lines  = open("journal.tmp").readlines();
write_lines    = [];


## Merge the Handwritten journal with machine generated
## into one file and copy it to the Output folder.
## Merge
for original_line in original_lines:
    if(original_line.replace(" ", "").replace("\n", "") == "__JOURNAL_DATA__"):
        for journal_line in journal_lines:
            write_lines.append(journal_line);
    else:
        write_lines.append(original_line);


index_file = open("Output/index.html", "w");
index_file.writelines(write_lines);
index_file.close();


## Clean up and temporaries created.
os.system("rm journal.tmp");
