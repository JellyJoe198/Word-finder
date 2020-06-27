## dictionary sorter 0.7.1
## GitHub repository: https://github.com/JellyJoe198/Word-sorter

from settings import *

## the base point value of each letter
worthiness = {'a': 1, 'b': 4, 'c': 4, 'd': 2, 'e': 1, 'f': 4, 'g': 3,
              'h': 3, 'i': 1, 'j': 10, 'k': 5, 'l': 2, 'm': 4, 'n': 2,
              'o': 1, 'p': 4, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 2,
              'v': 5, 'w': 4, 'x': 8, 'y': 3, 'z': 10}

# backwards compatability
try:
    x=leniency
    del x
except:
    print("You are using a depricated version. Attempting to correct input...")
    leniency = wrdLength - strictness

##prints a readout of what it is going to do
if (addOne):
    print('will find all', wrdLength, 'to', wrdLength+addOne, 'letter words from')
else:
    print('will find all', wrdLength, 'letter words from')
print(letters, '\nwith leniency of %s.'%(leniency))
if willScore:
    print('Also gives score to each word.')
print() # empty line

# checklength will check if the word is the right length
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

if addOne:
    def tempStrict(): # adjust strictness for wrdLength and addOne
        return L-wrdLength
else:
    def tempStrict():
        return False


tf = "dictionaries/filteredCombinedDict4a.txt" # input dictionary file
f = open(tf)
f.seek(0) # go to top of input file

our = "Output.%s" %(fileType) # the output file
with open(our,'a') as ur: # with output file open for writing/appending:
    ur.seek(0)
    if startLog:
        # put the settings at the beginning of the Output
        print('wrdLength = ', wrdLength, '\naddOne = ', addOne,
              '\nstrictness = ', strictness, '\nletters = ', letters,
              '\nrepeats = ', repeats, '\nrequired = ', required,
              '\nrequired_necessary = ', required_necessary, '\nrequired_preffered = ',
              required_preffered, '\nwillPrint = ', willPrint, '\nwillScore = ', willScore,
              '\nfileType = ', "'%s'" %(fileType), '\nstartLog = ', startLog,
              '\n#tf = ', "'%s'" %(tf), '\n#our = ', "'%s'" %(our), sep='', file=ur)

    for i in f: # for word in dictionary
        k = i.strip() # prevent empty lines, k is a line from the dictionary
        L = len(k) # read length of line
        if (checkLength(L)):
##            global tempLetters
            tempLetters = letters.copy() # once letters are found, it will remove it from this array
            yes = 0
            score = 0
##            used = [] # to be filled with letters that have been used
            for q in range(0, L): # check each character with each required letter
##                us = None # us will be the found letter?
                cha = k[q] # cha is character to be checked
                if(checkRequired(q)):
                    yes += 1 # add a match point
                    score = doScore()  # calculate score if scoring enabled
                elif(requirement(q)):
                    if cha in tempLetters:
                        yes += 1
                        score = doScore()
                        tempLetters.remove(cha) # remove one of the letter in temp array
            if (yes >= wrdLength - leniency + tempStrict()): # if found enough matches, put it in output
                writeAnswer() # print answer to Output or console

f.close()
print('\nfinished!')
