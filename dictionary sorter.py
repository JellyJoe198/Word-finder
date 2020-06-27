## dictionary sorter 0.6.5
## GitHub repository: https://github.com/JellyJoe198/Word-sorter
"""
wrdLength = 6 ## length of words to output
addOne = 1 ## how much longer than wrdLength will it also allow?
strictness = wrdLength -1  ## how many correct letters required (same as wrdLength)
## NOTE: for each blank, change strictness by -1

##put lowercase version of all possible letters here
#it is slightly more efficient if common letters are first.
letters = ['e','i','r','c'] ## EeIMRC_
##guide:  [ 0   1   2   3   4   5   6   7   8   9  10  11  12  13

##if a letter is repeated, put its location in letters[] here (starts at 0)
repeats = [0] ## (e)

## set a certain place to need a certain letter (blank string to ignore)
## Note: do not put in letters[] if it is in here unless it can repeat
## put an array to check multiple options for that slot like ['e','a','s']
required = {
    0:  'm',
    1:  '',
    2:  '',
    3:  '',
    4:  '',
    5:  '',
    6:  '',
    7:  '',
    8:  '',
    9:  '',
    10: '',
    11: '',
    12: '',
    13: '' }
required_necessary = True   # False if other letters can fill a required spot
required_preffered = False   # BOTH False to disable `required` check entirely

willPrint = True # print the words that it finds to console?
willScore = 1 # will it find the score? (0=no, 1=print only, 2=print and write)
fileType = 'null' # the file extension of Output (recommended: txt or csv)

startLog = True # put the settings used at the top of the Output?
"""

from settings import *
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
else:
    def checkLength(L):
        return L == wrdLength # this one takes less time when applicable

if required_necessary:
    def requirement(q):
        return required[q] == ''
##            return True
##        else:
##            return False
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
elif(fileType== 'null' or fileType== 'pyw'):
    def writeAnswer():
        readout() # print to console only
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


tf = "dictionaries/words_alpha.txt" # input dictionary file
f = open(tf)
f.seek(0) # go to top of input file

our = "Output.%s" %(fileType) # the output file
with open(our,'a') as ur: # with output file open for writing/appending:
    ur.seek(0)
    if startLog:
        # put the settings at the beginning of the Output
        print('wrdLength = ', wrdLength, '\naddOne = ', addOne, '\nstrictness = ', strictness, '\nletters = ', letters, '\nrepeats = ', repeats, '\nrequired = ', required, '\nrequired_necessary = ', required_necessary, '\nrequired_preffered = ', required_preffered, '\nwillPrint = ', willPrint, '\nwillScore = ', willScore, '\nfileType = ', "'%s'" %(fileType), '\nstartLog = ', startLog, '\n#tf = ', "'%s'" %(tf), '\n#our = ', "'%s'" %(our), sep='', file=ur)

    for i in f:
        k = i.strip() # prevent empty lines, k is a line from the dictionary
        L = len(k) # read length of line
        if (checkLength(L)):
            yes = 0 # number of correct letters
            score = 0 # points it would earn based on worthiness
            used = [] # to be filled with letters that have been used
            for q in range(0, L): # check each character with each required letter
                us = None # us will be the found letter?
                cha = k[q] # cha is character to be checked
                if(checkRequired(q)):
                    yes = yes+1 # add a match point
                    score = doScore()  # calculate score if scoring enabled
                elif(requirement(q)):
                    for a in range(0, len(letters)): # a in letters array
                        if (cha == letters[a]):
                            yes = yes+1 # add a match point
                            score = doScore()
                            us = a # record found letter
                            break # once a letter is found, stop searching

                if(us != None): # check if found letter is allowed to repeat
                    if not repeatable():
                        b = True
                        for a in used: # check if letter has been used
                            if(a == us):
                                b = False
                                break
                        if b:
                            used.append(us) # record letter has been used
                        else:
                            yes = yes-1 # revoke match point if letter already used

                if (yes >= strictness + tempStrict()): ## if found enough matches, put it in output
                    writeAnswer() # print answer to Output and console

f.close()
print('\nfinished!')
