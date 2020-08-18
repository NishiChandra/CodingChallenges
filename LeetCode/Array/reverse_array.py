#Reverse Array
#Time Complexity - O(N)
#Using two pointer technique

def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
    return arr
arr1 = [6,0,2,24,45,99,1]
result = reverseArray(arr1)
print(result)