#!/usr/bin/bash

read -p "Enter number of terms: " n

x=0
y=1

for ((i=1; i<=n; i++)); do
    echo -n "$x "
    temp=$((x + y))
    x=$y
    y=$temp
done

echo


