# Natural Solution

def stringCompression(word):
    listWord = []
    count = 1
    tupleWord = []
    for i in range(len(word) - 1):
        wordCurrent = word[i]
        if word[i] == word[i+1]:
            count += 1
        else:
            tupleWord.append(wordCurrent)
            tupleWord.append(count)
            count = 1
            listWord.append(tupleWord)
            tupleWord = []
    
    tupleWord.append(wordCurrent)
    tupleWord.append(count)
    listWord.append(tupleWord)

    strWord = ""
    for i in listWord:
        strWord += str(i[0])
        strWord += str(i[1])

    if len(word) < len(strWord):
        return word
    else:
        return strWord

word = input('Digite a palavra: ')

print(stringCompression(word))