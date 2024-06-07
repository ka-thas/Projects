def quickSort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = []
    right = []
    for i in range(1, len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])
    return quickSort(left) + [pivot] + quickSort(right)


print(quickSort([10, 6, 3, 4, 1, 2, 9]))
