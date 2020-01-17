# Natural Solution

def rotate(word1, word2):
    if len(word1) != len(word2):
        return False
    l1 = word1[0]
    found = False

    for i in range(len(word2)):
        if word2[i] == l1:
            found = True
            i2 = i
            break
    
    if not found:
        return False

    for i in range(len(word1)):
        offset = len(word1) - (len(word1) - i2 + 1)
        if i2 + i < len(word1):
            print(word1[i], word2[i2 + i])
            if word1[i] != word2[i2 + i]:
                return False
        else:
            print(word1[i], word2[i2 + i - len(word1)])
            if word1[i] != word2[i2 + i - len(word1)]:
                return False

    return True

# Tests

word1 = input('Digite a primeira palavra: ')
word2 = input('Digite a segunda palavra: ')

print(rotate(word1, word2))
