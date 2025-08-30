#!/usr/bin/bash

read -p "Enter Number: " x

if  ((x%2==0)) 
	then echo $((x+2))

else 
	echo $((x-5))
fi
