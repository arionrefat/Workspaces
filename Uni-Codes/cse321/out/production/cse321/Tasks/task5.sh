#!/usr/bin/env bash

read -r -p "Enter your numbers: " -a arr

echo Assending Order
sorted=($(printf '%s\n' "${arr[@]}" | sort -n))
echo ${sorted[@]}

echo Descending Order
sorted=($(printf '%s\n' "${arr[@]}" | sort -n -r))
echo ${sorted[@]}

#output should be like this 
# 1 4 5 6 8 1 10