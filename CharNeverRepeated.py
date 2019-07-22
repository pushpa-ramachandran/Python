# Find the char that is not repeated in a string. if more than, return the first repeated char

# if empty or too few return -1
# one by one, check the charcaters in dictionary. If found, add the count. Else add the char to dictionary
# Now iterrate thru the dictionary. Return the first char with count == 1
# if iteration completes, then it means that there is no unique char. return None

def findRepeatChar(str):
    # if empty or too few return -1
    if (len(str)) <= 1:
        return -1
    # one by one, check the charcaters in dictionary. If found, return the char. Else add the char to dictionary
    charDictionary = {}
    for ch in str.lower():
        if ch != " ":
            if ch in charDictionary:
                charDictionary[ch] += 1
            else:
                charDictionary[ch] = 1

    for c in str.lower():
        if c != " " and charDictionary[c] == 1:
            return c

    return "None"

# Scenarios
# with one repeated char
print('ab cd   e a- exp b')
print(findRepeatChar('ab cd   e a'))

# with multiple repeated chars
print('ab cd   ed  c b a -exp e')
print(findRepeatChar('ab cd   ed  c b a'))

# with lower and upper repeated chars
print('ab cd   e  E b a -exp c')
print(findRepeatChar('ab cd   e  E b a'))

# with no repeated char
print('ab cd   e - exp a')
print(findRepeatChar('ab cd   e'))

# with all repeated char
print('ab ab - exp None')
print(findRepeatChar('ab ab '))


# with empty str
print('Empty -Exp -1')
print(findRepeatChar(''))