#!/usr/bin/bash

arr=(5 10 15 20 25)
sum=0

for num in "${arr[@]}"; do
    ((sum += num))
done

echo "$sum"
