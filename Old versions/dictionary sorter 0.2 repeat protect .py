
wrdLength = 8 ## length of words to output, will also output this plus 1
strictness = 6 ## how many correct letters required {<}, should be wrdLength - 1

##put lowercase version of all possible letters here
letters = ['t','u','c','i','a','e'] ## TTU_CIA E  

##if a letter is repeated, put its location in letters[] here (starts at 0)
repeats = [0] ## T


##prints a readout of what it is going to do
print 'will find all', wrdLength, 'and', wrdLength+1, 'letter words with'
print(letters)
print 'in them, allowing'
for i in repeats:
    print(letters[i])
print 'to repeat with strictness of',strictness, '\n'

tf = "dictionaries/combined dictionary.txt" ## input dictionary file
f = open(tf)

our = "Output.txt" ## output file
##go to top of inputs
f.seek(0)
with open(our, 'a') as ur:
    ur.seek(0)

for i in f:
    k = i.strip() ##prevent empty lines
    
    with open("temp.txt", 'w+') as tem: ##makes temp file with current word
        tem.write(k)
        L = tem.tell()
        if (L == wrdLength ):##or L == wrdLength+1):   ## only use certain length words
            tem.seek(0)
            yes = 0 ## gets higher when a correct letter is found
            used = [] ## will be filled with letters that have been used
            for q in xrange(0, L):
                us = None
                cha = tem.read(1)
                for a in xrange(0, len(letters)): ##a in letters
                    if (cha == letters[a]): ##a):
                        yes = yes+1 ## add a match point
                        us = a
                    
                if(us != None):
                    able = False ## defaults to false unless in repeat list
                    for r in repeats: ## check if letter is allowed to repeat
                        if(us == r):
                            able = True
                    if able:
                        used.append(us)
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
##            print(k)
            if (yes > strictness): ## if found enough matches, put it in output
                with open(our, 'a') as ur:
                    ur.write(k + '\n')
                    print(ur.tell())
                    print(k)

f.close()
