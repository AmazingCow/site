#!/usr/bin/python
################################################################################
## file   : build.sh                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
################################################################################

index_source_filename = "../../index_original.html";
certs_source_filename = "../../certs.html";
index_target_filename = "../../index.html";


index_source = file(index_source_filename, "r").readlines();
certs_source = file(certs_source_filename, "r").readlines();

index_target = file(index_target_filename, "w");

for index_source_line in index_source:
    print index_source_line;
    if(index_source_line.replace("\n", "").lstrip(" ").rstrip(" ") != "__CERTS_PLACEHOLDER__"):
        index_target.write(index_source_line);
    else:
        for certs_source_line in certs_source:
            index_target.write(certs_source_line);

index_target.close();
