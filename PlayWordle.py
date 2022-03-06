from termcolor import colored

myfile=open("wordle-answers-alphabetical.txt",'r')
myfile2=open("wordle-allowed-guesses.txt",'r')
wordlist=myfile.readlines()+myfile2.readlines()

#Naive Approach, just pick all words close enough to the green values. if no green values, then just pick words with those yellow values in them

def getManhattanScore(word,info,banned):
    c=0
    if len(word)!=5:
        return -1
    for x in range(len(word)):
        if info[x][0]==word[x] and info[x][1]==2:#If matching and green
            c+=2
        elif info[x][0] in word and info[x][1]==1 and info[x][0] not in banned[word.index(info[x][0])]:
            #If exists, yellow and isnt already guessed in that location before
            c+=1            
        elif word[x] in banned[x]: #If its a banned letter, then reduce the score (We've tried it before and it was gray)
            c-=1
        #ELSE match but not green, or exists but not yellow, or doesnt exist
        #Then dont do anything (c+=0)
    return [c,banned]


def getGuess(infoGained,allGuesses,banned):
    global wordlist
    if infoGained[0][0]==-1 and infoGained[0][1]==-1:
        #First guess, just guess CRANE cause i like it
        return ['crane',banned]
    #Otherwise, make use of the info found and lets find similar words:


    for x in range(len(banned)):
        if infoGained[x][1]==0:#if a letter is gray, ban it from everywhere
            for i in range(len(banned)):
                banned[i].append(infoGained[x][0])
        elif infoGained[x][1]==1: #If the letter is yellow, only ban it from the current location
            banned[x].append(infoGained[x][0])
    
    scores=[]
    for word in wordlist:
        word=word.strip()
        if word in allGuesses:
            continue
        s,banned=getManhattanScore(word,infoGained,banned)
        scores.append([word,s])
    
    scores.sort(reverse=True, key= lambda x:x[1])
    print(scores[:10])
    return ([scores[0][0],banned])

# ------------------------------------------------ GAME HERE -------------------------------------------
numguesses=0
guess="aaaaa"
allGuesses=[]
banned=[[],[],[],[],[]] #Store all letters that are banned in a given location
infoGained=[[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]] #0,1,2 -> Gray,Yellow,Green
found=False
while numguesses<6 and not found:
    
    res=getGuess(infoGained,allGuesses,banned)
    guess,banned=res[0],res[1]

    print("Guess:",guess)
    allGuesses.append(guess)

    #User makes the guess on the platform theyre playing on
    #Report back the color of each letter as prompted:
    # 0->Gray, 1->Yellow, 2->Green

    for i in range(len(guess)):
        infoGained[i][0]=guess[i]
        infoGained[i][1]=int(input(f"Enter color of {guess[i]}: "))

    found=True
    for x in range(len(infoGained)):
        if infoGained[x][1]!=2:
            found=False

    numguesses+=1
    
