#!/usr/bin/env bash

# Write a shell script which takes 10 integers as input from the user. Then calculate the sum of those integers which are multiple of 2 but not multiple of 8. Print the sum as an output.

read -r -p "Enter your Values: " -a arr
echo "You entered: ${arr[@]}"
