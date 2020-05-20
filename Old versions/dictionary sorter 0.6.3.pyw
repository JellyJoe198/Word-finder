
wrdLength = 7 ## length of words to output
addOne = 1 ## how much longer than wrdLength will it also allow?
strictness = wrdLength #-1  ## how many correct letters required (same as wrdLength)
## NOTE: for each blank, change strictness by -1

##put lowercase version of all possible letters here
#it is slightly more efficient if common letters are first.
letters = ['e','d','b','g','r','u'] ## DEBUGgeR
##guide:  [ 0   1   2   3   4   5   6   7   8   9  10  11  12  13

##if a letter is repeated, put its location in letters[] here (starts at 0)
repeats = [0,3] ## (g,e)

## set a certain place to need a certain letter (0 to ignore)
## Note: do not put in letters[] if it is in here unless it can repeat
## put an array to check multiple options for that slot like ['e','a','s']
required = {
    0:  ['p','h'],
    1:  ['p','h'],
    2:  ['p','h'],
    3:  ['p','h'],
    4:  '0',
    5:  '0',
    6:  '0',
    7:  '0',
    8:  '0',
    9:  '0',
    10: '0',
    11: '0',
    12: '0',
    13: '0' }
required_necessary = False  # False if other letters can fill a required spot
required_preffered = True   # BOTH False to disable `required` check

willPrint = True ##print the words that it finds to console?
willScore = 0 ##will it find the score? (0=no, 1=print only, 2=print and write)
fileType = 'csv' # the file extension of Output (recommended: txt or csv)

## the base point value of each letter
worthiness = {'a': 1, 'b': 4, 'c': 4, 'd': 2, 'e': 1, 'f': 4, 'g': 3,
              'h': 3, 'i': 1, 'j': 10, 'k': 5, 'l': 2, 'm': 4, 'n': 2,
              'o': 1, 'p': 4, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 2,
              'v': 5, 'w': 4, 'x': 8, 'y': 3, 'z': 10}

##prints a readout of what it is going to do
if (addOne):
    print('will find all', wrdLength, 'to', wrdLength+addOne, 'letter words with')
else:
    print('will find all', wrdLength, 'letter words with')
print(letters, 'in them,')
if repeats:
    print('allowing')
    for i in repeats:
        print(letters[i],end=', ')
    print('to repeat')
print('with strictness of %s.' % (strictness))
if willScore:
    print('Also gives score to each word.')
print()

##checklength will check if it is the right length, and changes based on addOne
##so we don't have to check addOne all the time (time optimization)
if addOne:
    def checkLength(L):
        return(L >= wrdLength and L <= wrdLength+addOne)
##        if(L >= wrdLength and L <= wrdLength+addOne):
##            return True
##        else:
##            return False
else:
    def checkLength(L):
        return L == wrdLength # this one takes less time when applicable
##        if(L == wrdLength):
##            return True
##        else:
##            return False


if required_necessary:
    def requirement(q):
        if required[q]=='0':
            return True
        else:
            return False
    def checkRequired(q):
        try:
            for e in required[q]: # check required letters for that position
                if e==cha:
                    return True
        except:
            return False
else:
    def requirement(q):
        return True
    if required_preffered:
        def checkRequired(q):
            try:
                for e in required[q]: # check required letters for that position
                    if e==cha:
                        return True
            except:
                return False
    else:
        def checkRequired(q):
            return False


if willPrint and willScore:
    def readout():
        print(k, score, sep='  —  ')  # show word and its score
elif willPrint:
    def readout():
        print(k)  # show word only
else:
    def readout():
        return False

if willScore==2:
    def writeAnswer():
        print(k, score, sep=',', file=ur) # write the word and score to ur in csv format
        readout() # print to console
else:
    def writeAnswer():
        print(k, file=ur) # write the word to ur
        readout() # print to console


if willScore:
    def doScore():
        return score + worthiness[cha]
else:
    def doScore():
        return False

def repeatable():
    for r in repeats: # check if letter is allowed to repeat
        if(us == r):
            return True
    return False

if addOne:
    def tempStrict(): # adjust strictness for wrdLength and addOne
        return L-wrdLength
else:
    def tempStrict():
        return False


tf = "dictionaries/filteredCombinedDict4a.txt" ## input dictionary file
f = open(tf)

##go to top of input file
f.seek(0)

our = "Output.%s" %(fileType)
with open(our, 'a') as ur:
    ur.seek(0)

    for i in f:
        k = i.strip() ##prevent empty lines, k becomes 1 line from the dictionary

        L = len(k) ##read length of line
        if (checkLength(L)):
            yes = 0 ##number of correct letters
            score = 0 ##points it would earn
            used = [] ## will be filled with letters that have been used
            for q in range(0, L): ##check each character with each required letter
                us = None
                cha = k[q] ##cha is character to be checked
                if(checkRequired(q)):
                    yes = yes+1 ## add a match point
                    score = doScore()  ##calculate score if scoring enabled
                elif(requirement(q)):
                    for a in range(0, len(letters)): ##a in letters array
                        if (cha == letters[a]):
                            yes = yes+1 ## add a match point
                            score = doScore()
                            us = a
                            break ##once it finds a letter, stop searching

                if(us != None): ##checks if letter is allowed to repeat
                    if not repeatable():
                        b = True
                        for a in used: ## check if letter has been used
                            if(a == us):
                                b = False
                                break
                        if b:
                            used.append(us) ##record letter has been used
                        else:
                            yes = yes-1 ## remove the match point it it already used

                if (yes >= strictness + tempStrict()): ## if found enough matches, put it in output
##                    with open(our, 'a') as ur:
##                    ur.write(k + '\n')
##                    print(k, file=ur) # this is the same as ur.write
                    writeAnswer() # print answer to Output and console
##                    readout()

f.close()
print('\nfinished!')
