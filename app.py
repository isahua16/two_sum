nums = [3, 3] 
target = 6

def two_sum(arr, target):
    for i in range(len(nums)):
        for y in range(len(nums)):
            if(nums[i] + nums[y] == target and i != y):
                return [nums[i], nums[y]]

print(two_sum(nums, target))

