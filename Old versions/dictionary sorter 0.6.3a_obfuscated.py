#dictionarySorter 0.6.3a obfuscated+compact
#GitHubRepository:https://github.com/JellyJoe198/Word-sorter
wrdLength=6#LengthWords2Output
addOne=1#HowMuchLongerThan wrdLength toAlsoAllow?
strictness=wrdLength -1 #HowManyCorrectLettersRequired.4eachBlank,changeStrictnessBy -1
letters=['e','t','l','g','u']#lowercaseVersionFAllPossibleLettersHere
repeats=[]#ifALetterIsRepeated,putItsLocationN letters[] here
#SetAcertainPlace2needACertainLetter(blankString2Ignore)
#Note:doNotPutNLetters[]IfItIsHereNlessItCanRepeat
#putAnArray2checkManyOptions4thatSlot:['e','a','s']
required = {
    0:	'',
    1:	'',
    2:	'',
    3:	'',
    4:	'',
    5:	'',
    6:	's',
    7:	'',
    8:	'',
    9:	'',
    10:	'',
    11:	'',
    12:	'',
    13:	'' }
required_necessary=True#FalseIfOtherLettersCanFillA'required'spot
required_preffered=True#bothFalsetodisable'required'checkentirely

willPrint=True#printTheWords2console
willScore=0#willItFindScore(0=no,1=printonly,2=printandwrite)
fileType='null'#fileXtensionOf Output

nnn={'a':1,'b':4,'c':4,'d':2,'e':1,'f':4,'g':3,'h':3,'i':1,'j':10,'k':5,'l':2,'m':4,'n':2,'o':1,'p':4,'q':10,'r':1,'s':1,'t':1,'u':2,'v':5,'w':4,'x':8,'y':3,'z':10}
if (addOne):
    print('will find all',wrdLength,'to',wrdLength+addOne,'letter words with')
else:
    print('will find all',wrdLength,'letter words with')
print(letters,'in them,')
if repeats:
    print('allowing')
    for i in repeats:
        print(letters[i],end=', ')
    print('to repeat')
print('with strictness of %s.' % (strictness))
if willScore:
    print('Also gives score to each word.')
print()
if addOne:
    def aa(L):
        return(L>=wrdLength and L<=wrdLength+addOne)
else:
    def aa(L):
        return L==wrdLength
def ffff():
    try:
        for e in required[q]:
            if e==lll:
                return True
    except:
        return False
if required_necessary:
    def bb(q):
        return required[q]==''
    def cc(q):
        return ffff()
else:
    def bb(q):
        return True
    if required_preffered:
        def cc(q):
            return ffff()
    else:
        def cc(q):
            return False
if willPrint and willScore:
    def dd():
        print(k,iii,sep='  —  ')
elif willPrint:
    def dd():
        print(k)
else:
    def dd():
        return False
if willScore==2:
    def ee():
        print(k,iii,sep=',',file=ur)
        dd()
else:
    def ee():
        print(k,file=ur)
        dd()
if willScore:
    def ff():
        return iii+nnn[lll]
else:
    def ff():
        return False
def gg():
    for r in repeats:
        if(us==r):
            return True
    return False
if addOne:
    def hh():
        return L-wrdLength
else:
    def hh():
        return False
f=open("dictionaries/filteredCombinedDict4a.txt")
f.seek(0)
our="Output.%s" %(fileType)
with open(our,'a')as ur:
    ur.seek(0)
    for i in f:
        k=i.strip()
        L=len(k)
        if (aa(L)):
            jjj=0
            iii=0
            mmm=[]
            for q in range(0, L):
                us=None
                lll=k[q]
                if(cc(q)):
                    jjj=jjj+1
                    iii=ff()
                elif(bb(q)):
                    for a in range(0, len(letters)):
                        if (lll==letters[a]):
                            jjj=jjj+1
                            iii=ff()
                            us=a
                            break
                if(us!=None):
                    if not gg():
                        b=True
                        for a in mmm:
                            if(a==us):
                                b=False
                                break
                        if b:
                            mmm.append(us)
                        else:
                            jjj=jjj-1
                if (jjj>=strictness+hh()):
                    ee()
f.close()
print('\nfinished!')
