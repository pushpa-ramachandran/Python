# In an integer array, find the pairs of values that would add up to the sum ‘s’
# [1,3,4,6,7,9,11] –sum 10 – pairs, (3,7), (4,6), (1,9)

# check whether list has atleast 2 numbers
# iterate thru the numbers
# find the other part to the sum - x-s
# if not yet in 'seen' set
# save the x in the 'seen' set
# otherwise add the target and x to the output set

def pairs(arr, sum):
    seen =set()
    output = set()

    if(len(arr) < 2):
        print('List has very few numbers')
    else:
        for x in arr:
            target = sum-x

            if target not in seen:
                seen.add(x)
            else:
                output.add((min(x,target),max(x,target)))

    print('Pairs ' ,output)

print('########[1,3,4,6,7,9,11] , 10')
pairs([1,3,4,6,7,9,11] , 10)
print('########[1] , 10')
pairs([1] , 10)
print('######## [] , 10')
pairs([] , 10)
print('######## [1,3,-1,3,5] , 0')
pairs([1,3,-1,3,5] , 0)

#############################################################################

####### Find the maximum continous sum in an array

## Start with the index 0 and iterate
# Assume that number at index 0 is the maxSum and currentSum
# move to next and add to the current sum
# compare currentSum and maxSum and swap if currentSum is > than the maxSum

def findMaxSum(arr):
    length = len(arr)

    # check for too few numbers
    if length <=1:
        print('Too few numbers. Can not find MaxSum')
        return

    # Assume that number at index 0 is the maxSum and currentSum
    maxSum = currentSum = arr[0]

    ### Start with the index 0 and iterate
    i=1
    while( i < length):
        # move to next and add to the current sum
        currentSum += arr[i]

        # compare currentSum and maxSum and swap if currentSum is > than the maxSum
        print(' current sum and maxsum ', currentSum, maxSum)
        if currentSum > maxSum:
            maxSum = currentSum
        i+=1

    return maxSum

print('[7,1,2,-1,3,4,10,-12,3,21,-19] expected result 38')
print(findMaxSum([7,1,2,-1,3,4,10,-12,3,21,-19]))
print('[1,2,3,4,5,-1,-2] expected result 15')
print(findMaxSum([1,2,3,4,5,-1,-2]))
print('[-1,-2] expected result -1')
print(findMaxSum([-1,-2]))
print('[1] expected result ‘Very few numbers’') #to be handled
print(findMaxSum([1]))





