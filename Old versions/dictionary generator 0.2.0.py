##put bad characters here
##letters = ['-',"'",'1','2','3','4','5','6','7','8','9','0'] ## -' 1234567890
##letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
##           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] ## CAPITALIZED
##letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
##           'n','o','p','q','r','s','t','u','v','w','x','y','z'] ## lowercase
letters = ['.','&','/'] ## . & / 

tf = "dictionaries/filteredCombinedDict2.txt" ## input dictionary file
f = open(tf)

our = "OutputDict.txt" ## output file

f.seek(0) ##go to top of inputs

with open(our, 'a') as ur:
    ur.seek(0) ##initiate output file

for i in f:
    k = i.strip() ##prevent empty lines, k is a line of the dictionary

    L = len(k) ##length of word
    found = False ##default to not found
    for q in range(0, L): ##check each character with each required letter
        cha = k[q]
        for a in range(0, len(letters)): ##a in letters array
            if (cha == letters[a]): ##a):
                found = True ## flag it

    if (found == False): ## if not found a match, put it in output
        with open(our, 'a') as ur:
            ur.write(k + '\n')
##            print(ur.tell())
##            print(k)
##    else:
##        print(k)

f.close()
