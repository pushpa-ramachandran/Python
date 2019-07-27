##########Selection Sort. Sorts by repeatedly finding the minimum element (considering ascending order)
# from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
#
# Time Complexity - O(n **2). Space complexity - O(1). Good for small datasets

#Arrays to be sorted
arr1 = [5,6,7,8,1,2,3,4]
arr = [9]

def selectionsort(a):

    # Iterate starting from 0 to last but one element
    for k in range(0,len(a)-1,1):

        # Iterrate stating from the next element to k
        # Assume that it is the min element
        # Iterate till last element and compare it with k'th element
        # If small, swap it with kth element

        for min in range (k+1,len(a),1):

            if a[k] > a[min]:
                temp = a[k]
                a[k] = a[min]
                a[min] = temp

    return a

print(arr , "- ")
print(selectionsort(arr))

print(arr1 , "- ")
print( selectionsort(arr1))

