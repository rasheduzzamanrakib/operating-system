#!/usr/bin/bash

read -p "Enter a number: " n
fact=1

for ((i=2; i<=n; i++)); do
    ((fact *= i))
done

echo "$fact"
