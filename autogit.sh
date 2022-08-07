#!/bin/bash

while true; do
    git add . && git commit -m "[ADD] Auto push from shell file" && git push
    RANDOM=$$
    echo $RANDOM >> number.txt
    git gc --auto

done