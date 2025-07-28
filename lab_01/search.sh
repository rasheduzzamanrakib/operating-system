#!/usr/bin/bash

arr=(3 7 9 2 5 8)

read -p "Enter a number to search: " x

for i in "${arr[@]}"; do
    if (( i == x )); then
        echo "Found"
        exit
    fi
done

echo "Not Found"
