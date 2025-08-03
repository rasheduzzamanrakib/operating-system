#!/usr/bin/bash
ls -l

arr={1..20}

for num in $arr
do 
    echo $num
    sleep 0.5
done
