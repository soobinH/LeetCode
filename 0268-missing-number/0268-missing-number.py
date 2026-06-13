class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        answer = 0

        if max(sorted_nums) != n:
            return max(sorted_nums)+1


        else:

            for i in range(1, n):
                if sorted_nums[i] - sorted_nums[i-1] == 2:
                    answer = sorted_nums[i]-1

        

            return answer


