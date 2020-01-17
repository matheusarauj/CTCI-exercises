# Natural Solution

def oneEdit(word1, word2):
    count1 = []
    count2 = []
    for i in range(256):
        count1.append(0)
        count2.append(0)
    
    for i in word1:
        count1[ord(i)] += 1

    for i in word2:
        count2[ord(i)] += 1

    edit = 0
    for i in range(256):
        if count1[i] == count2[i] and count1[i] != 0:
            edit += 1
            
    largerWord = max(len(word1), len(word2))
    if largerWord - edit > 1:
        return False

    return True

# Tests

word1 = input('Digite a primeira palavra: ')
word2 = input('Digite a segunda palavra: ')

print(oneEdit(word1, word2))