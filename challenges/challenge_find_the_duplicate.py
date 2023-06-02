def find_duplicate(nums):
    repeated = []
    merge_sort(nums)
    for i in range(len(nums) - 1):
        if len(nums) < 2 or type(nums[i]) is not int or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1] and nums[i] not in repeated:
            repeated.append(nums[i])
    if len(repeated) == 1:
        return repeated[0]
    else:
        return False


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
