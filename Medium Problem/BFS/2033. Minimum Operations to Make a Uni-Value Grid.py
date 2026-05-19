class Solution(object):
    def minOperations(self, grid, x):
        
        # Step 1: Flatten grid
        nums = []
        for row in grid:
            nums.extend(row)

        # Step 2: Check feasibility
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1

        # Step 3: Sort numbers
        nums.sort()

        # Step 4: Choose median
        median = nums[len(nums) // 2]

        # Step 5: Count operations
        operations = 0
        for num in nums:
            operations += abs(num - median) // x

        return operations