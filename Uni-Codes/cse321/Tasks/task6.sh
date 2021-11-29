read num
result=$num

happy_prime()
{
    result=$1
    count=0
    while [ $result -gt 0 ]; do
        rem=$(( $result % 10 ))
        a=$(( $rem * $rem ))
        count=$(( $count + $a ))
        result=$(( $result / 10 ))
    done
    echo "$count"
}

for (( i=0; i<num; i++ ))
do
    result=$(happy_prime $result)
done

if [ $result == 1 ]; then
      echo "Happy number"
    else
      echo "Not a happy number"
fi
