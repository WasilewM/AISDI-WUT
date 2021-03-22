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
            result.append(chr(index))
        index += 1

    return result
