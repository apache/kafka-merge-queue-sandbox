#!/bin/bash

for FILE in `git diff-index --name-status origin/main -- | cut -c3-` ; do
    if grep -q 'FAILQUEUE' "$FILE"
    then
        echo $FILE ' contains FAILQUEUE!'
        exit 1
    fi
done
exit 
