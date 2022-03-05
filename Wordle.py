from termcolor import colored

myfile=open("wordle-answers-alphabetical.txt",'r')
myfile2=open("wordle-allowed-guesses.txt",'r')
wordlist=myfile.readlines()+myfile2.readlines()

#Naive Approach, just pick all words close enough to the green values. if no green values, then just pick words with those yellow values in them

def getManhattanScore(word,info):
    c=0
    if len(word)!=5:
        return -1
    for x in range(len(word)):
        if info[x][0]==word[x] and info[x][1]==2:#If matching and green
            c+=2
        elif info[x][0] in word and info[x][1]==1:#If exists and yellow
            c+=1
        #ELSE match but not green, or exists but not yellow, or doesnt exist
        #Then dont do anything (c+=0)
    return c


def getGuess(infoGained,allGuesses):
    global wordlist
    if len(infoGained[0])==0:
        #First guess, just guess EARTH cause i like it
        return 'earth'
    #Otherwise, make use of the info found and lets find similar words:
    scores=[]
    for word in wordlist:
        word=word.strip()
        if word in allGuesses:
            continue
        scores.append([word,getManhattanScore(word,infoGained)])
    
    scores.sort(reverse=True, key= lambda x:x[1])
    #print(scores)
    print(scores[:10])

    return scores[0][0]

# ------------------------------------------------ GAME HERE -------------------------------------------
secret="brine"
numguesses=0
guess="aaaaa"
allGuesses=[]
infoGained=[[],[],[],[],[]] #0,1,2 -> Red,Yellow,Green
while numguesses<=6 and guess!=secret:
    
    #guess=input("Enter guess:")
    while(len(guess)!=5):
        print("Invalid guess. Must have 5 letters exactly")
        input("Enter guess:")

    guess=getGuess(infoGained,allGuesses)
    print("Guessing:",guess)
    allGuesses.append(guess)
    for i in range(len(guess)):
        if secret[i]==guess[i]:
            infoGained[i]=[guess[i],2]
            print(colored(guess[i],'green'),end="")
        elif guess[i] in secret:
            infoGained[i]=[guess[i],1]
            print(colored(guess[i],'yellow'),end="")
        else:
            infoGained[i]=[guess[i],0]
            print(colored(guess[i],'white'),end="")
    print()
    numguesses+=1
    



