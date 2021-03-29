def quick_sort(my_list):
    smaller = []
    equal = []
    bigger = []
    if len(my_list) > 1:
        pivot = my_list[0]
        for item in my_list:
            if item > pivot:
                bigger.append(item)
            elif item < pivot:
                smaller.append(item)
            else:
                equal.append(item)
        return quick_sort(smaller) + equal + quick_sort(bigger)
    else:
        return my_list
