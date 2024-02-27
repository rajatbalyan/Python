# Explanation
# https://youtu.be/Eipu0MqwS2s

class Solution:
    def twoSum(self, nums, target):
        seen={} #created a hashmap
        i=0
        while i<len(nums):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [i,seen[complement]]
            seen[num]=i
            i+=1