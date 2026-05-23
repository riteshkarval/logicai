
def smaller_number_after(nums: list):
    smaller_nums = []
    len_nums = len(nums)
    for i in range(len_nums):
        c = 0
        for j in range(i+1, len_nums):
            if nums[j] < nums[i]:
                c += 1
        smaller_nums.append(c)
    return smaller_nums

print(smaller_number_after(nums = [5, 2, 6, 1]))

print(smaller_number_after(nums = [1]))
