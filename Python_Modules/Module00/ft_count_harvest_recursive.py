def ft_count_harvest_recursive():
    print("Days until harvest:", end=" ")
    value = int(input())

    def recursion(start, value):
        if (start > value):
            print("Harvest time!")
            return
        print(f"Day {start}")
        recursion(start + 1, value)
    recursion(1,value)

ft_count_harvest_recursive()
