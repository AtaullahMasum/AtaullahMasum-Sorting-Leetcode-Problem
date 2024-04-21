def cyclicSort(nums):
    i , n = 0, len(nums)
    while i < n:
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    return nums
nums = [3, 5, 2, 1, 4]
result = cyclicSort(nums)

