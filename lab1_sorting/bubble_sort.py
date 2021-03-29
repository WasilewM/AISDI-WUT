def bubble_sort(my_list):
    for item in my_list:
        for index in range(len(my_list) - my_list.index(item) - 1):
            if my_list[index] > my_list[index + 1]:
                my_list[index], my_list[index + 1] = my_list[index+1], my_list[index]
    return my_list
