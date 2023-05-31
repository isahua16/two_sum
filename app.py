nums = [3,3] 
target = 6

def two_sum(arr, target):
    for num in nums:
        for number in nums:
            if(num + number == target):
                solution = []
                solution.insert(0, nums.index(number))
                solution.insert(0, nums.index(num))
                return solution

print(two_sum(nums, target))

