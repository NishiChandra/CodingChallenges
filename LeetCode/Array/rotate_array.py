#Rotate Array by n places
'''
Step 1 : Divide array into n-r and r

Step 2 : Reverse n-r and r
 
Step 3 : Reverse whole array
'''
def reverseArray(arr,start,end):
    while start < end :
        arr[start],arr[end] = arr[end],arr[start]
        start = start + 1
        end = end - 1


def rotateArray(arr,r):
    if r == 0:
        return arr
    n = len(arr)
    end = n - r
    reverseArray(arr,0,end-1)
    print("1",arr)
    reverseArray(arr,end,n-1)
    print("2",arr)
    reverseArray(arr,0,n-1)
    print("3",arr)
    return arr

arr1 = [4,6,2,5,1]
result = rotateArray(arr1,0)
print(result)
