#!/bin/sh

# Creates a series of directories, provided
# that they don't already exist
createDirectories() {
    for dir in $1
    do
        mkdir -p -- "$dir"
    done
}

createDirectories "counting-function"
