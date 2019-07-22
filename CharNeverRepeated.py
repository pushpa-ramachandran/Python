# Find the char that is not repeated in a string. if more than, return the first repeated char

# if empty or too few return -1
# one by one, check the charcaters in dictionary. If found, return the char. Else add the char to dictionary
# if iteration completes, then it means that there is no repeat char. return None

def findRepeatChar(str):
    # if empty or too few return -1
    if (len(str)) <= 1:
        return -1
    # one by one, check the charcaters in dictionary. If found, return the char. Else add the char to dictionary
    charDictionary = {}
    for ch in str:
        if ch != " ":
            if ch in charDictionary:
                return ch
            else:
                charDictionary[ch] = 1

    return "None"

# Scenarios
# with one repeated char
print('ab cd   ed a- exp a')
print(findRepeatChar('ab cd   e a'))

# with multiple repeated chars
print('ab cd   ed  c b a -exp c')
print(findRepeatChar('ab cd   e  c b a'))

# with no repeated char
print('ab cd   ed - exp None')
print(findRepeatChar('ab cd   e'))


# with empty str
print('Empty -Exp -1')
print(findRepeatChar(''))