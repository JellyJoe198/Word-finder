
wrdLength = 7  ## length of words to output
addOne = 0 ## how much longer than wrdLength will it also allow?
strictness = wrdLength #-1  ## how many correct letters required (same as wrdLength)
## NOTE: for each blank, change strictness by -1

##put lowercase version of all possible letters here
#it is slightly more efficient if common letters are first. 
letters = ['h','y','n','i','g','o','t','u','e'] ## HY NIGO TUE
##guide:  [ 0   1   2   3   4   5   6   7   8   9  10  11  12  13

##if a letter is repeated, put its location in letters[] here (starts at 0)
repeats = [] ## (none)

## set a certain place to need a certain letter (0 to ignore)
## Note: do not put in letters[] if it is in here unless it can repeat
## put an array to check multiple options for that slot like ['e','a','s']
required = {
    0:  ['a','g'],
    1:  ['n','g','l','c','t'],
    2:  ['i'],
    3:  ['e','i','l','s','t','c'],
    4:  ['o'],
    5:  ['i','r','t','e'],
    6:  ['c','l'],
    7:  '0',
    8:  '0',
    9:  '0',
    10: '0',
    11: '0',
    12: '0',
    13: '0' }
required_necessary = False  ##False if other letters can fill a required spot
required_preffered = True   ##BOTH False to disable `required` check

willPrint = True ##print the words that it finds?
willScore = False ##will it find the score? (may be irrelevant if willPrint is False)

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
        print(letters[i])
    print('to repeat')
print('with strictness of', strictness)

print('Also gives score to each word.\n')


##checklength will check if it is the right length, and changes based on addOne
##so we don't have to check addOne all the time (time optimization)
if addOne:
    def checkLength(L):
        if(L >= wrdLength and L <= wrdLength+addOne):
            return True
        else:
            return False
else:
    def checkLength(L):
        if(L == wrdLength): ##this one takes less time when applicable
            return True
        else:
            return False


if required_necessary:
    def requirement(q):
        if required[q]=='0':
            return True
        else:
            return False

    def checkRequired(q):
    ##    if required[q][0]==cha:
    ##        return True
    ##    else:
        try:
            for e in range(len(required[q])):
    ##            print(e)
                if required[q][e]==cha:
    ##                print(e)
                    return True
        except:
            return False
else:
    def requirement(q):
        return True
    if required_preffered:
        def checkRequired(q):
            try:
                for e in range(len(required[q])):
        ##            print(e)
                    if required[q][e]==cha:
        ##                print(e)
                        return True
            except:
                return False
    else:
        def checkRequired(q):
            return False


if willPrint and willScore:
    def readout():
        print(k, '  ', score)## show word and its score
elif willPrint:
    def readout():
        print(k)## show word only
else:
    def readout():
        return False


if willScore:
    def doScore():
        return score + worthiness[cha]
else:
    def doScore():
        return 0



tf = "dictionaries/filteredCombinedDict5.txt" ## input dictionary file
f = open(tf)

##go to top of input file
f.seek(0)

our = "Output.txt" ## output file
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
                    able = False
                    for r in repeats: ##check if letter is allowed to repeat
                        if(us == r):
                            able = True
                            break
##                    if able:
##                        used.append(us) ##record the letter has been used (not needed here because the letter can repeat anyways)
                    if not able:
                        b = True
                        for a in used: ## check if letter has been used
                            if(a == us):
                                b = False
                                break
                        if b:
                            used.append(us) ##record letter has been used
                        else:
                            yes = yes-1 ## remove the match point it it already used
    ##            print(used)
    ##            print(k) ## print the word

                if (yes >= strictness): ## if found enough matches, put it in output
##                    with open(our, 'a') as ur:
                    ur.write(k + '\n')
                    readout()


f.close()
