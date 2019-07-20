###### Check whether the strings are anagrams, 2 strings with exact letters

def anagram(str1, str2):
    return sorted(str1.replace(' ','').lower()) == sorted(str2.replace(' ','').lower())

print(anagram("abc", "A B C"))
print(anagram("abc", "AbcC"))

###### Optimized version
# count up the letters in str1
# count down the letters in str2
# if count != 0 then not anagrams
# else anagrams

print('Anagram_Optimized')
def anagramOptimzed(str1, str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ', '').lower()
    print(str1 , " & ", str2)
    count ={} # initiate an empty dictionary to count
    # if the lengths are not equal, they are not anagrams

    # print( 'Leng ', len(str1), ' & ',len(str2 ))
    if(len(str1) != len(str2)):
        return False
    #count up for str1
    for c in str1:
        if c in count:
            count[c]+=1
        else:
            count[c] =1

    #count down for str2
    for c in str2:
        if c in count:
            count[c]-=1
        else:
            count[c]=1

    #Check the counts. if not Zero, then not Anagrams
    for x in count:
        if count[x] != 0:
            return False

    #If it has reached this level, then they are anagrams
    return True

print(anagramOptimzed("abc","ABC"))
print(anagramOptimzed("abc","ABCd"))
print(anagramOptimzed("abc",""))
print(anagramOptimzed(",","ABC"))

