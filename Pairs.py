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