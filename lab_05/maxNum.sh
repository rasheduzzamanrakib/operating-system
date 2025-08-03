#!/usr/bin/bash

arr=(15 22 9 48 3 76 31)
max=${arr[0]}

for num in "${arr[@]}"; do
    if (( num > max )); then
        max=$num
    fi
done

echo "The maximum number is: $max"
