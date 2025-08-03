#!/usr/bin/bash

arr=(10 20 30 40 50)

for (( i=${#arr[@]}-1; i>=0; i-- )); do
    echo "${arr[i]}"

done
