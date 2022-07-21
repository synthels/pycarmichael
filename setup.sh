#!/bin/sh

# Creates a series of directories, provided
# that they don't already exist
createDirectories() {
    local -n dirs=$1
    for dir in "${dirs[@]}"
    do
        mkdir -p -- "$dir"
    done
}

directories=("counting-function" "gaps") 
createDirectories directories
