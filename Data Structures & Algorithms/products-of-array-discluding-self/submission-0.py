class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = [1]
        end = [1]

        for i in range(len(nums)-1): 
            start.append(start[i]*nums[i])

        rnums = nums[::-1]
        for i in range(len(rnums)-1):
            end.append(end[i]*rnums[i])
        end = end[::-1]

        '''print(start)
        print(end)'''

        result = []
        for i in range(len(nums)):
            result.append(start[i]*end[i])

        return result