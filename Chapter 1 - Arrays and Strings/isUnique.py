# Natural Solution

def isUnique(word):
    if len(word) > 256:
        return False

    booleans = []
    for i in range(256):
        booleans.append(False)
    
    for i in word:
        if not booleans[ord(i)]:
            booleans[ord(i)] = True
        else:
            return False
    
    return True

# No additional data structure:

def isUniqueNoData(word):
    if len(word) > 256:
        return False

    for i in range(len(word)):
        for j in range(len(word)):
            if i != j and word[i] == word[j]:
                return False
    
    return True

# Test
word = input('Digite a palavra: ')

print(isUnique(word))
print(isUniqueNoData(word))


