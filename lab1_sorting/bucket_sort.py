def bucket_sort(table):
    items_quantity = []

    while len(items_quantity) < 256:
        items_quantity.append(0)

    for item in table:
        items_quantity[ord(item)] += 1

    result = []
    index = 0
    for item in items_quantity:
        if item != 0:
            char_quantity = 0
            while char_quantity < item:
                result.append(chr(index))
                char_quantity += 1
        index += 1

    return result
