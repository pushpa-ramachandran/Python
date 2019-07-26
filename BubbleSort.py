#########Bubble sort - Large element bubbles up to the top. Time Complexity - O(n **2). Space complexity - O(1)

# iterate thru the list and compare the previous element with the current element. If the previous is bigger, then swap the element
# After one iteration, the largetst element is at the end. Now iterate again starting from 0 to last but one element. (reduce n by 1 for every iterration)
# Continue it until all the elements are sorted.


arr1 = [5,6,7,8,1,2,3,4]
arr = [3,1,2,3,4]

def bubblesort(arr):

    n = len(arr)

    while n >= 1:

        for i in range (1,n,1):

            if arr[i-1] > arr[i]:

                temp = arr[i-1]
                arr[i-1]= arr[i]
                arr[i] = temp

        n -= 1

    return arr


print(bubblesort(arr))

print(bubblesort(arr1))
