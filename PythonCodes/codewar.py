def pyramid(n):
    list1 = []

    for i in range(0, n):
        list2 = []
        for j in range(0, i):
            list2.append(1)

        list1.append(list2)

    print(list1)


pyramid(3)
