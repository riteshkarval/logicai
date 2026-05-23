

def num_subarr_sum_k(nums:list, k:int):
    subarr = []
    len_nums = len(nums)
    for i in range(len_nums):
        if nums[i] == k:
            subarr.append([k])
            continue
        if i < len_nums -1:
            if nums[i] + nums[i+1] == k:
                subarr.append([nums[i], nums[i+1]])
    print(subarr)
    return len(subarr)

print(num_subarr_sum_k(nums = [1,1,1], k=2))

print(num_subarr_sum_k(nums = [1, 2, 3], k=3))