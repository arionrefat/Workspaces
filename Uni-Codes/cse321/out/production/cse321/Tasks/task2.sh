read -r -p "Enter a number: " nums

if [ $((nums % 4)) -ne 0 ] && [ $((nums % 5)) -ne 0 ] && [ $((nums % 10)) -eq 0 ]; then
    echo "Rasengan"
fi

if [ $((nums % 5)) -eq 0 ] || [ $((nums % 6)) -eq 0 ]; then
    if [ $((nums % 5)) -eq 0 ] && [ $((nums % 6)) -eq 0 ]; then
        :
    else
        echo "Odama Rasengan"
    fi
fi

if [ $((nums % 5)) -eq 0 ] && [ $((nums % 6)) -eq 0 ]; then
    echo "Rasen Shuriken"
fi
