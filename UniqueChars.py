# check whether string has all the unique characters

#uniqueChars

#check for empty string
#if not empty, move the chars one by one to dictionary. If not already available, add with 1 count.
# else increment the count
#once done. iterate thru the dic, to find numbers more than one


def uniqueChars(str):
    # check for empty string
    if len(str) <= 1:
        return -1

    # if not empty, move the chars one by one to dictionary. If not already available, add with 1 count.
    # else increment the count
    chars = {}
    spaces = " "
    for ch in str:
        if ch in spaces:
            continue

        if ch in chars:
            return False
        else:
            chars[ch] = 1

    return True

# uniqueChars using BuiltIn functions in python
# use replace to replace the spaces, use set(str) and find lhe length. Compare it with the original str length
def uniqueCharsBuiltIn(str):
    if len(str) <=1:
        return -1
    str = str.replace(' ', '')
    return len(str) == len(set(str))


#Scenarios
# String with unique chars
# String with non-unique chars
# Emtpy string

# String with unique chars
print( 'String with unique chars - Exp - True')
print(' uniqueChars -', uniqueChars("abc de f"))
print('uniqueCharsBuiltIn - ',uniqueCharsBuiltIn("abc de f"))

# String with non-unique chars
print( 'String with Non-unique chars - Exp - False')
print(' uniqueChars -', uniqueChars("abc abc"))
print('uniqueCharsBuiltIn - ',uniqueCharsBuiltIn("abc abc"))

# Emtpy string
print( 'String with no chars - Exp - Too few chars or empty')
print(' uniqueChars -', uniqueChars(""))
print('uniqueCharsBuiltIn - ',uniqueCharsBuiltIn(""))