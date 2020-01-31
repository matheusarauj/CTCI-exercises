# Natural Solution

def mostThree(word):
    c1 = word[0]
    c2 = word[1]
    c3 = word[2]
    cont = 0
    dic = {}

    while(cont < len(word) - 3):
        key = c1 + c2 + c3
        if(dic.__contains__(key)):
            dic[key] += 1
        else:
            dic[key] = 1

        cont += 1
        c1 = word[0 + cont]
        c2 = word[1 + cont]
        c3 = word[2 + cont]

    maior = 0
    seq = ""

    for i in dic:
        if(dic[i] > maior):
            maior = dic[i]
            seq = i

    return seq, maior

# Tests 

word = input("Digite a palavra: ")

print(mostThree(word))