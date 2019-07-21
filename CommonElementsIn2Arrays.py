# Common elements in 2 sorted(ascending) arrays
# [1,2,3,4,5,6,7,8,10,11,12,15] and [6,7,8,9,10,11,12,13] – common [6,7,8,10,11,12]
#
#

# no initail validaitons
# since they are sorted, start with 0 from both. compare. if list1 is smaller number, then iterate list1 till it beoomes or equal than list2
# whichever is smaller, iterate it
def findCommon(arr1, arr2):
    length1 = len(arr1)
    length2 = len(arr2)
    i1 = 0
    i2 = 0
    common = []
    while (i1 < length1 and i2 < length2):
        if ( arr1[i1] < arr2[i2]):
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            i2 += 1
        else:
            common.append(arr2[i2])
            i1 += 1
            i2 += 1
    return common


print('[1,2,3,4,5,6,7,8,10,11,12,15] and [6,7,8,9,10,11,12,13] – common [6,7,8,10,11,12]')
print(findCommon( [1,2,3,4,5,6,7,8,10,11,12,15] , [6,7,8,9,10,11,12,13]))

print('[1,2,3,4,5] and [3,4,5,6,7,8,9,10,11,12,13] – common [3,4,5,13]')
print(findCommon( [1,2,3,4,5,13] , [3,4,5,6,7,8,9,10,11,12,13]))

#No common elements
print('[1,2,3,4,5]and [6,7,8,9,10,11,12,13] – common []')
print(findCommon( [1,2,3,4,5] , [6,7,8,9,10,11,12,13]))

#not sorted - not a valid TC. As the problem itself says that the lists are sorted
print('[1,2,3,9,4,5]and [6,7,8,1,9,10,11,12,13] – common []')
print(findCommon( [1,2,3,9,4,5] , [6,7,8,1,9,10,11,1,12,13]))