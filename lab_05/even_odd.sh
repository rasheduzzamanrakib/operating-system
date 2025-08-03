#!/usr/bin/bash

arr=(1 2 3 4 5 6 7 8 9 10)

echo "Even numbers:"
for num in "${arr[@]}"; do
    if ((num % 2 == 0)); then
        echo "$num"
    fi
done

echo "Odd numbers:"
for num in "${arr[@]}"; do
    if ((num % 2 != 0)); then
        echo "$num"
    fi
done
