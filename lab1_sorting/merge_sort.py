def merge_sort(table):
    """
    Funciton is an implementation of merge sort algorithm.
    """
    if len(table) == 1:
        return table

    half_idx = int(len(table) / 2)
    left_half = table[:half_idx]
    right_half = table[half_idx:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    left_ptr = right_ptr = 0
    result = []
    length_sum = len(left_half) + len(right_half)

    while (left_ptr + right_ptr) < length_sum:
        if left_ptr < len(left_half):
            if right_ptr < len(right_half):
                if left_half[left_ptr] < right_half[right_ptr]:
                    result.append(left_half[left_ptr])
                    left_ptr += 1
                else:
                    result.append(right_half[right_ptr])
                    right_ptr += 1
            else:
                result.append(left_half[left_ptr])
                left_ptr += 1
        elif right_ptr < len(right_half):
            result.append(right_half[right_ptr])
            right_ptr += 1
    return result
