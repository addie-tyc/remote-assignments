def two_sum(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        hash_table[nums[i]] = i
        
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            if hash_table[target - nums[i]] != i:
                return [i, hash_table[target-nums[i]]]
    return []
