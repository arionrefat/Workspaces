#!/usr/bin/env bash

read -r -p "Enter an array: " -a arr
sums=0

if [ ${#arr[*]} -gt 10 ]; then
    echo you have entered more than 10 characters
else
    for i in {0..10}; do
        if [ $((arr[i] % 2)) -eq 0 ] && [ $((arr[i] % 8)) -ne 0 ]; then
            sums=$((arr[i]+sums))
        fi
    done
    echo "Total Sum: ${sums}"
fi

#input should be like this
# 2 3 4 9 0 8 0 ..
