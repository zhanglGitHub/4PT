#!/bin/bash

for ip in $(seq 199 254); do
ping -c1 192.168.1.$ip |grep "bytes from" |cut -d" " -f 4 | cut -d":" -f 1 & 
done
