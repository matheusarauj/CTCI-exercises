# Natural Solution

def palindromePermutation(word):
    count = []
    for i in range(256):
        count.append(0)

    for i in word:
        if i != " ":
            count[ord(i)] += 1
    
    odd = 0
    for i in count:
        if i%2 != 0:
            odd += 1
        
    if odd > 1:
        return False
    else:
        return True

# Test

word = input("Digite a palavra: ")

print(palindromePermutation(word))