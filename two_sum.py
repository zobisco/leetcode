from pip import List

def twoSum(nums: List[int], target: int) -> List[int]:        
    visited = {}
    for idx, number in enumerate(nums):
        desired_number = target - number
        if desired_number in visited:
            return [nums.index(desired_number), idx]
        else:
            visited[number] = True


print(twoSum([2, 7, 11, 15], 9))

# EOF
