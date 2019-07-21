# check whethers 2 ordered arrays are rotated version of the other. [1,2,3,4,5] and [3,4,5,1,2]

# check the lengths of the 2 lists. if not equal, return False
# take the first from list1 and iterate and find the index from list2... equal to the first element from list1
# start from 0 in the list1 and start from index2 +j+1 % len(list1) from list2.
# iterate compare. if all are not equal - False

def checkRoation(list1, list2):
    # check the lengths  of the 2 lists. if not equal, return False
    if len(list1) != len(list2):
        return False

    for i in range(0,len(list1),1):
        if list2[i] == list1[0]:
            index2 = i
            break

    # start from 0 in the list1 and start from index2 +j+1 % len(list1) from list2.
    length = len(list1)
    for j in range(len(list1)):

        i2 = ((index2 + j+1) %  length)
        # iterate compare. if all are not equal - False
        if list1[j] != list2[i2]:
            return False

    # Iterated thru the entire lists. There is no inequality. Hence return True
    return True

#equal and rotated
#not equal - to be checked initially
# equal but not rotated

#equal and rotated
print('equal and rotated - [1,2,3,4,5] and [3,4,5,1,2] - Exp - True')
print(checkRoation([1,2,3,4,5] , [3,4,5,1,2]))

#not equal - to be checked initially
print('not equal [1,2,3,4,5] and [4,5,1,2] - exp False')
print(checkRoation([1,2,3,4,5] , [3,4,5,1,2]))

# equal but not rotated
print('equal but not rotated [1,2,3,4,5] and [4,3,5,1,2] - Exp - False')
print(checkRoation([1,2,3,4,5] , [3,4,5,1,2]))