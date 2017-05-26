#!/bin/bash

echo "--> Update Repositories";
## COWFIX: We have a bogus download repo script....
## It currently aren't update the repos correctly,
## so for now we gonna delete and clone each time...
rm -rf amazingcow_repos;
mkdir -p amazingcow_repos;

./download_repos.py
