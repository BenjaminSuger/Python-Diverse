def ft_count_harvest_iterative():
    print("Days until harvest:", end=" ")
    value = int(input())
    for i in range(0, value + 1):
        print(f"Day {i}")
    print("Harvest time!")


ft_count_harvest_iterative()
