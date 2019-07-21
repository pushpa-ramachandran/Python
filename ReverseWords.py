##### Reverse words in the sentence

##### with python libraries - reversed
def reverse(str):
    return " ". join(reversed(str.split()))

##### reverseStartEndReverse
def reverseStartEndReverse(str):
    return " ". join((str.split())[::-1])

##### Writing code to split and join in reverse

def reverseCode(str):
    words=[]
    wordsR = []

    length = len(str)
    space =" "
    startCh = -1
    i=0
    # iterate thru the string till the length
    while i < length:
        if str[i] not in space:
            startCh = i

            while i< length and str[i] not in space:
                i+=1

            # arrived at the end space, move the characters from startCh to endCh to words
            words.append(str[startCh:i])
        i+=1

    #split the words. Combine them in reverse order
    wordsCount = len(words)
    for j in range(wordsCount-1,-1,-1):
        print(j)
        wordsR.append(words[j])

    print(wordsR)
    return " ".join(wordsR)


print("Wish you happy birth day")
print('Using Reversed - ' ,reverse("Wish you happy birth day"))
print('Using reverseStartEndReverse - ' ,reverseStartEndReverse("Wish you happy birth day"))
print('Using reverseCode - ' ,reverseCode("Wish you happy birth day"))

print("GM")
print('Using Reversed - ',reverse("GM"))
print('reverseStartEndReverse - ',reverseStartEndReverse("GM"))
print('reverseCode - ',reverseCode("GM"))

print("empty string")
print('Using Reversed - ' ,reverse(""))
print('Using reverseStartEndReverse - ' ,reverseStartEndReverse(""))
print('Using reverseCode - ' ,reverseCode(""))



