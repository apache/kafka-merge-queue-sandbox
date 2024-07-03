#!/bin/bash

for FILE in `git diff-index --name-status origin/main -- | cut -c3-` ; do
    if grep -q 'FAIL' "$FILE"
    then
        echo $FILE ' contains FAIL!'
        exit 1
    fi
done
exit 
