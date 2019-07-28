##########Merge Sort. Divide and Conquer algorithm that works recursively dividing the array into 2 halves and sorting and merging them back
# Divide the arr into 2 halves Left and Right Recursively
# Base condition is to check whether the length of array is greater than 1
# For either the length of Left or Right arrays, keep on comparing left and right arrays.
# Move the smallest of the two to the main array
# Check for any remaining elements in both  the arrays to accomodate for any missed elements
# Time complexity - nLog(n)- Space complexity - n
# Faster and fit for larger arrays

def MergeSoft(a) :

    if(len(a)> 1):

        mid = int(len(a)/2)

        Left = a[:mid]
        Right = a[ mid:]

        MergeSoft(Left)
        MergeSoft(Right)

        leftIter =rightIter = k =0
        while leftIter < len(Left) and rightIter < len(Right):
            if Left[leftIter] < Right[rightIter]:
                a[k] =Left[leftIter]
                leftIter += 1
            else:
                a[k] =Right[rightIter]
                rightIter += 1
            k += 1

        while( leftIter < len(Left)):
            a[k] =(Left[leftIter])
            leftIter += 1
            k += 1

        while( rightIter < len(Right)):
            print(Right[rightIter])
            a[k] =(Right[rightIter])
            rightIter += 1
            k += 1

a = [2,4,6,8, 1,3,5,7,0,10,11]

MergeSoft(a)
print(a)