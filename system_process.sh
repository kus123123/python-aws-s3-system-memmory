#!/bin/bash

echo $time >>available-memmory.txt
a=$(free -h | grep Mem | awk '{print $7}')

echo "available memory before clearing cache: $a" >>available-memmory.txt

sudo sync; echo 3 > /proc/sys/vm/drop_caches 

b=$(free -h | grep Mem | awk '{print $7}')

echo "available memory after clearing cache: $b " >>available-memmory.txt


