txt = str(input())
listwords = txt.split()
newlist = []
for i in range(0,len(listwords)):
    newlist.append(listwords[i][0])
num = 0
alphabets = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
alphabets_occurence = []
for i in range(0,19):
    for j in range(0,len(newlist)):
        if alphabets[i] == newlist[j]:
            num=num+1
    alphabets_occurence.append(num)
    num = 0
isAAlliteration = 0
character = ''
times = 0
for i in range(0,19):
    if alphabets_occurence[i] >= 2:
        isAAlliteration = 1 
        character = alphabets[i]
        times = alphabets_occurence[i]
        break
        
if isAAlliteration == 1:
    print(f"The sentence above is an Alliteration since the sound of the consonant {character} is repeated for {times} times.\n")
else:
    print(f"The sentence above is not an Alliteration\n")