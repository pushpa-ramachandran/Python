# What is the most frequently occurring element in array [ 1, 1, 1, 3, 4, 5]


# check for null or too few
# create a dictionary for each element
# iterrate and check whether the element is already in dictionary. if not, add with the number -1, else increase the count
# come out of the lopp and loop thru the dictionary
# assume that the first element is the highest- currentMax. Compare against the other numbers and swap if the count is greater than the currentMax

def findFreqElement(arr):
    # check for null or too few
    length = len(arr)
    if length <= 1:
        return 'Too few elements'
    else:
        # create a dictionary for each element
        elements = {}
        i = 0
        # iterrate and check whether the element is already in dictionary. if not, add with the number -1, else increase the count
        for i in arr:
            if i in elements:
                #increase the count
                elements[i] += 1
            else:
                # add the element with 1 value
                elements[i] = 1


        # assume that the first element is the highest- currentMax.
        # Compare against the other numbers and swap if the count is greater than the currentMax
        max = 0
        element = None
        for j in elements:
            if elements[j] >= max:
                max = elements[j]
                element = elements[max]

        # if the max is not greater than one, it means that there is repetition. hence return -1
        if max > 1:
            return element
        else:
            return -1

#Scenarios
# Array with most frequently occuring element - [ 1, 1, 1, 3, 4, 5]
print(' [ 1, 1, 1, 3, 4, 5] - Exp 1')
print(findFreqElement([ 1, 1, 1, 3, 4, 5]))

# Array with most frequently occuring element - [ 1, 1, 1, 3, 4,4,4,5,4, 5]
print(' [1, 1, 1, 3, 4,4,4,5,4, 5] - Exp 4')
print(findFreqElement([ 1, 1, 1, 3, 4,4,4,5, 5]))

# Array with one element or null
print(' Array with no element - Exp - Array has too few or no elemnents')
print(findFreqElement([]))

# Array with no repetive numbers - [1,2,3,4,5]
print( 'Array with no repetive numbers - [1,2,3,4,5] - Exp - No elements repeated')
print(findFreqElement([ 1, 3, 4, 5]))
