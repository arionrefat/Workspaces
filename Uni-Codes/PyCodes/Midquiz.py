def function(x):
    if (x == 0 or x == 1):
        print("stop")
    else:
        print(x)

    return function(x%2)

print(function(15))
