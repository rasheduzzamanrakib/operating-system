#!/usr/bin/bash

arr=(-3 0 7 -1 4 0 9 -8)

pos=0
neg=0
zero=0

for num in "${arr[@]}"; do
    if (( num > 0 )); then
        ((pos++))
    elif (( num < 0 )); then
        ((neg++))
    else
        ((zero++))
    fi
done

echo "Positive: $pos"
echo "Negative: $neg"
echo "Zero: $zero"
