#!/usr/bin/env bash

read -r -p "Enter three numbers: " -a arr

function one_g_two {
    if [ $((arr[0])) -gt $((arr[1])) ];then
        echo $((arr[0] - arr[1]))
    fi
}

function two_l_one {
    if [ $((arr[2])) -lt $((arr[1])) ];then
        echo $((arr[2] + arr[1]))
    fi
}

function one_eq_two {
    if [ $((arr[1])) -eq $((arr[2])) ];then
        echo $((arr[1] * arr[2]))
    fi
}

if [ ${#arr[*]} -gt 3 ]; then
    echo you have entered more than 10 characters
else
    one_g_two
    two_l_one
    one_eq_two
fi

#output should be like this
#3 4 1