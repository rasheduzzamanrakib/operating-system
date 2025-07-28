#!/usr/bin/bash

read -p "Enter a number: " n

if (( n <= 1 )); then
    echo "Not Prime"
    exit
fi

for (( i=2; i*i<=n; i++ )); do
    if (( n % i == 0 )); then
        echo "Not Prime"
        exit
    fi
done

echo "Prime"
