# Natural Solution

def urlify(word):
    nWord = ""
    for i in word:
        if i == " ":
            nWord += '%20'
        else:
            nWord += i

    return nWord

# Test

word = input('Digite a palavra: ')

print(urlify(word))


