#!/bin/bash

read -p "Enter file name: " fname
read -p "Enter the search pattern: " pattern
if [ -f "$fname" ]
then
    result=$(grep -i "$pattern" "$fname")
    echo "$result"
fi

# Another grep choices 
# cat  file | grep "open" | cut -d "/" -f1 
# cat  file | grep "open" | cut -d "/" -f1 | sort -u | tr '\n' ','

