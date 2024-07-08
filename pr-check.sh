#!/bin/bash

for FILE in `git diff-index --name-status origin/main -- | cut -c3-` ; do
    if grep -q 'FAILPR' "$FILE"
    then
        echo $FILE ' contains FAILPR!'
        exit 1
    fi
done
exit 
