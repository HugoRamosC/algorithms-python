def is_anagram(first_string: str, second_string: str):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_sorted = list(first_string.lower())
    second_sorted = list(second_string.lower())
    merge_sort(first_sorted)
    merge_sort(second_sorted)
    first_sorted = ''.join(first_sorted)
    second_sorted = ''.join(second_sorted)

    return (first_sorted, second_sorted, first_sorted == second_sorted)


def merge_sort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)
        merge(list, start, mid, end)


def merge(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            list[general_index] = right[right_index]
            right_index = right_index + 1
