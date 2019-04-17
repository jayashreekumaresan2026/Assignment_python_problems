#https://leetcode.com/problems/rotate-array/
def rotate():
    nums = [1, 2]
    k = 3
    n = len(nums)
    k = abs(k % n)
    if k != 0:
        nums[k:], nums[:k] = nums[:n - k], nums[n - k:]
        return nums

print(rotate())
