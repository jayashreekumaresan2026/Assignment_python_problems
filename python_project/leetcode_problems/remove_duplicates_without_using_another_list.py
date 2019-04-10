#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates():
    nums=[0,0,1,1]
    lst = sorted(list(set(nums)))
    l = len(lst)
    for i in range(l):
        nums[i] = lst[i]
    return l
print(removeDuplicates())