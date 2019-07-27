##########Insertion Sort. Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
# Iterate from 1 to len(a) - current
# Compare the current with the previous
# if the current is less than the previous, swap
# Continue this backwards, till the element 1, previous--, next--
# Time Complexity - O(n **2). Space complexity - O(1). Good for small datasets

#Arrays to be sorted
arr1 = [5,6,7,8,1,2,3,4]
arr = [9]
arr2 = [4,4,4,5,1,8]

def insertionsort(a):

    # Iterate from 1 to len(a) - current
    for current in range(1,len(a),1):
        previous = current -1
        next=current

        while(previous >= 0):

            #Compare the current with the previous
            if a[previous] > a[next]:

                # if the current is less than the previous, swap
                temp=a[previous]
                a[previous] =a[next]
                a[next]= temp

            # Continue this backwards, till the element 1, previous--, next--
            previous = previous - 1
            next = next - 1

    return a

print(arr , "- ")
print(insertionsort(arr))

print(arr1 , "- ")
print( insertionsort(arr1))

print(arr2 , "- ")
print( insertionsort(arr2))

