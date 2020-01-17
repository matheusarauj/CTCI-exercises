# Natural Solution

def checkPermutation(string1, string2):
    booleans = []
    attemps = []
    for i in range(256):
        booleans.append(False)
        attemps.append(0)

    for i in string1:
        booleans[ord(i)] = True
        attemps[ord(i)] += 1

    for i in string2:
        if attemps[ord(i)] > 1:
            attemps[ord(i)] -= 1
        elif booleans[ord(i)] and attemps[ord(i)] == 1:
            booleans[ord(i)] = False
        else:
            return False
    
    return True

# Test

string1 = input('Digite a primeira palavra: ')
string2 = input('Digite a segunda palavra: ')

print(checkPermutation(string1, string2))