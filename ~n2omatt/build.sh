#!/bin/bash

################################################################################
## Helper Functions                                                           ##
################################################################################
call_build_script()
{
    ./$1/build.sh
}

copy_build_script_output()
{
    mkdir -p ./Output/$1;
    cp -rf ./$1/Output/* ./Output/$1
}

## Special Functions for Index / Certs
call_build_script_index_and_certs()
{
    ./build_index_and_certs.sh
}

copy_build_script_output_index_and_certs()
{
    mkdir -p ./Output

    cp index.html ./Output
    cp -rf certs ./Output
}



## Clean up
rm -rf ./Output
mkdir -p ./Output

## Call the inner build scripts.
call_build_script journal
call_build_script lectures
call_build_script resume

call_build_script_index_and_certs


## Copy the output of the inner build scripts.
copy_build_script_output journal
copy_build_script_output lectures
copy_build_script_output resume

copy_build_script_output_index_and_certs
