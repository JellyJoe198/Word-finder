
wrdLength = 8  ## length of words to output
addOne = 0 ## will it also output wrdLength + 1 ?
strictness = wrdLength -2  ## how many correct letters required (same as wrdLength)
## NOTE: for each blank, change strictness by -1

##put lowercase version of all possible letters here
letters = ['r','i','n','s'] ## RISiNs      
##guide:  [ 0   1   2   3   4   5   6   7   8   9  10  11  12  13

##if a letter is repeated, put its location in letters[] here (starts at 0)
repeats = [1,3] ## (I, S)


## the base point value of each letter
worthiness = {
    'a':1,
    'b':4,
    'c':4,
    'd':2,
    'e':1,
    'f':4,
    'g':3,
    'h':3,
    'i':1,
    'j':10,
    'k':5,
    'l':2,
    'm':4,
    'n':2,
    'o':1,
    'p':4,
    'q':10,
    'r':1,
    's':1,
    't':1,
    'u':2,
    'v':5,
    'w':4,
    'x':8,
    'y':3,
    'z':10}


##prints a readout of what it is going to do
if (addOne):
    print('will find all', wrdLength, 'and', wrdLength+1, 'letter words with')
else:
    print('will find all', wrdLength, 'letter words with')
print(letters)
print('in them, allowing')
for i in repeats:
    print(letters[i])
print('to repeat with strictness of', strictness)
print('Also gives score to each word.\n')


tf = "dictionaries/filteredCombinedDict.txt" ## input dictionary file
f = open(tf)

our = "Output.txt" ## output file
##go to top of input file
f.seek(0)
with open(our, 'a') as ur:
    ur.seek(0)

for i in f:
    k = i.strip() ##prevent empty lines, k becomes 1 line from the dictionary

##    print(len(k))
    L = len(k) ##read length of line

    rightLength = False
    if (addOne):
        if (L == wrdLength or L == wrdLength+1):
            rightLength = True
    else:
        if (L == wrdLength):
            rightLength = True
    
    if (rightLength): 
        yes = 0 ##number of correct letters
        score = 0 ##points it would earn
        used = [] ## will be filled with letters that have been used
        for q in range(0, L): ##check each character with each required letter
            us = None
            cha = k[q] ##cha is character to be checked
            for a in range(0, len(letters)): ##a in letters array
                if (cha == letters[a]):
                    yes = yes+1 ## add a match point
                    score = score + worthiness[cha]
                    us = a
                    
            if(us != None): ##checks if letter is allowed to repeat
                able = False
                for r in repeats: ##check if letter is allowed to repeat
                    if(us == r):
                        able = True
                if able:
                    used.append(us) ##record the letter has been used
                else:
                    b = True
                    for a in used: ## check if letter has been used
                        if(a == us):
                            b = False
                    if b:
                        used.append(us)
                    else:
                        yes = yes-1 ## remove the match point
##            print(used)
##            print(k) ## print the word

            if (yes >= strictness): ## if found enough matches, put it in output
                with open(our, 'a') as ur:
                    ur.write(k + '\n')
##                    print(ur.tell()) ##print location in output
                    print(k, '  ', score)## show word and its score


f.close()
