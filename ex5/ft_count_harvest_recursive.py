def ft_count_harvest_recursive():
    def helper(day, a):
        if day > a:
            print("Harvest time")
            return
        print("Day", day)
        helper(day + 1, a)

    a = int(input("Days until harvest: "))
    helper(1, a)
