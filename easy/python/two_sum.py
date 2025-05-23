# Question (https://leetcode.com/problems/two-sum/)
# --------
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]



# Approach
# --------

def answer(nums, target):
    num_to_index = {} # maintain a hash table to store the difference of the target and the current number along with the index of the current number.
    for index, num in enumerate(nums): # iterate throught the list of numbers and find the complement,

        complement = target - num # find the complement

        if complement in num_to_index:
            # if the complememt is present in the hash table then return the index of the complement and the current index.
            return [num_to_index[complement], index]
        # else add the current number and its index to the hash table.
        num_to_index[num] = index
    return []
 