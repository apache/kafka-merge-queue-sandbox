#!/bin/bash

for FILE in `git diff-index --name-status origin/main -- | cut -c3-` ; do
    if grep -q 'QFAIL' "$FILE"
    then
        echo $FILE ' contains QFAIL!'
        exit 1
    fi
done
exit 
