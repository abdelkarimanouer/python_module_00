def ft_count_harvest_recursive():
    def recurse():
        pass
    days = int(input("Days until harvest: "))
    i = 1
    if i <= days:
        print("Day", i)
        i += 1
        ft_count_harvest_recursive()
    else :
        return ;

ft_count_harvest_recursive()