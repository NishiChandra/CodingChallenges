'''
move zeros : this is solved using two pointer technique 
we take two pointers i and j 
->i is kept as 0
->j iterates over length of nums
swap elements when nums[j] is not equal to zero in this way all the zeros will be placed at the end
increase i
if nums[j] is zero increase j
'''
def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0 :
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
        else:
            j = j + 1
    print(nums)

arr = [0,0,1,2,5,6,0,9]
moveZeroes(arr)
