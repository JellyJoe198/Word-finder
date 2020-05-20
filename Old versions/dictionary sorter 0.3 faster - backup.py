
wrdLength = 7  ## length of words to output
addOne = False ## will it also output wrdLength + 1 ?
strictness = 6 ## how many correct letters required {<}, should be wrdLength - 1

##put lowercase version of all possible letters here
letters = ['q','a','i','p','n','u','t'] ## QAIPNUT

##if a letter is repeated, put its location in letters[] here (starts at 0)
repeats = [] ## (none)


##prints a readout of what it is going to do
if (addOne):
    print 'will find all', wrdLength, 'and', wrdLength+1, 'letter words with'
else:
    print 'will find all', wrdLength, 'letter words with'
print(letters)
print 'in them, allowing'
for i in repeats:
    print(letters[i])
print 'to repeat with strictness of', strictness, '\n'

tf = "dictionaries/combined dictionary.txt" ## input dictionary file
f = open(tf)

our = "Output.txt" ## output file
##go to top of inputs
f.seek(0)
with open(our, 'a') as ur:
    ur.seek(0)

for i in f:
    k = i.strip() ##prevent empty lines, k is a line of the dictionary

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
        used = [] ## will be filled with letters that have been used
        for q in xrange(0, L): ##check each character with each required letter
            us = None
            cha = k[q]
            for a in xrange(0, len(letters)): ##a in letters array
                if (cha == letters[a]): ##a):
                    yes = yes+1 ## add a match point
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
                    

##    with open("temp.txt", 'w+') as tem: ##makes temp file with current word
##        tem.write(k)
##        L = tem.tell() ##L = length of word
##        if (L == wrdLength or L == wrdLength+1): ## only use certain length words
##            tem.seek(0)
##            yes = 0 ## gets higher when a correct letter is found
##            used = [] ## will be filled with letters that have been used
##            for q in xrange(0, L):
##                us = None
##                cha = tem.read(1)
##                for a in xrange(0, len(letters)): ##a in letters array
##                    if (cha == letters[a]): ##a):
##                        yes = yes+1 ## add a match point
##                        us = a
##                    
##                if(us != None): ##
##                    able = False ## defaults to false unless in repeat list
##                    for r in repeats: ## check if letter is allowed to repeat
##                        if(us == r):
##                            able = True
##                    if able:
##                        used.append(us)
##                    else:
##                        b = True
##                        for a in used: ## check if letter has been used
##                            if(a == us):
##                                b = False
##                        if b:
##                            used.append(us)
##                        else:
##                            yes = yes-1 ## remove the match point

##            print(used)
##            print(k)

            if (yes > strictness): ## if found enough matches, put it in output
                with open(our, 'a') as ur:
                    ur.write(k + '\n')
                    print(ur.tell())
                    print(k)

f.close()
