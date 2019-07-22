# Return ALL unique chars in a string

# Check for empty - too few - mix of small and upper

# AllUnique
def AllUnique(str):
    if len(str.replace(" ", "").lower()) <= 1:
        return -1


    # Dictionary of chars and counts
    charDict = {}
    unique =[]
    for ch in str.lower():
        if ch in charDict:
            charDict[ch] += 1
        else:
            charDict[ch] = 1

    for c in charDict:
        if charDict[c] == 1:
            unique.append(c)

    if not unique:
        return "None"
    else:
        return unique

#Scenarios
# All unique
print("ab   cd  - Exp - abcd")
print(AllUnique("ab   cd  "))

# One unique
print("ab   cd ab   c  - Exp - d")
print(AllUnique("ab   cd ab   c  "))

# No unique
print("ab   ab  - Exp - None")
print(AllUnique("ab   ab  "))

# Empty
print("  - Exp - Too few or empty ")
print(AllUnique("  "))

# Non Unique upper and lower
print("ab   AB  - Exp - ab")
print(AllUnique("ab   AB  "))

