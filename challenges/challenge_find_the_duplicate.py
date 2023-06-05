def find_duplicate(nums):
    repeated = []
    nums.sort()
    for i in range(len(nums) - 1):
        if len(nums) < 2 or type(nums[i]) is not int or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1] and nums[i] not in repeated:
            repeated.append(nums[i])
    if len(repeated) == 1:
        return repeated[0]
    else:
        return False
