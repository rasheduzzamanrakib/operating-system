#!/usr/bin/bash

arr=(10 20 30 40 50)
sum=0

for i in "${arr[@]}"; do
  ((sum += i))
done

avg=$((sum / ${#arr[@]}))
echo "$avg"
