#!/bin/bash


echo -n "Enter filename: "
read filename
for name in $(< $filename); do 
host "$name" | grep "has address" | awk '{print $4}' >> file.txt; cat file.txt | sort | uniq > $filename.ips;
#host $name |grep "has address" | cut -d" " -f4 >> file.txt | sort | uniq > file.txt
#>> file.txt; cat file.txt | sort | uniq > ip4domains.txt
done
rm -rf file.txt 

