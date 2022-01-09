#!/usr/bin/env bash

read -r -p "Enter a Number: " nums

sums () {
  local -i n="$1" sum=0

  while ((n)); do
    d=n%10
    sum+=d*d
    n=n/10
  done

  echo "$sum"
}

is_happy () {
  local -i n="$1" seen=()

  while ((n != 1)); do
    if [ -n "${seen[$n]}" ]; then #if the length of nonzaeo
      return 1
    fi

    seen[n]=1
    let n="$(sums "$n")"
  done

  return 0
}

happyNum () {
  if is_happy "$nums"; then
    echo "$nums" is a Happy Prime Number
  else
    echo Not Happy Prime Number
  fi
}

happyNum
