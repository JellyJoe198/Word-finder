## UI version 0.1 for dictionary sorter version 0.6.5
from settings_blank import *

##change the output name to "settings.pyw" to use it in the sorter

y=True
n=False

def bolea(query):
    a = input('%s = bool('%(query))
    if a=='.':
        return
    elif int(a) == 0:
        return False
    else:
        return True
def inter(query):
    a = input('%s = int('%(query))
    if a=='.':
        return
    try:
        return a
    except:
        return int(input('please enter an integer. %s:'%(query)))

if bolea("Do you want to import from settings.pyw?"):
    print("Importing settings.pyw:\n")
    from settings import *

print('wrdLength = ', wrdLength,
      '\naddOne = ', addOne,
      '\nstrictness = ', strictness,
      '\nletters = ', letters,
      '\nrepeats = ', repeats,
      '\nrequired = ', required,
      '\nrequired_necessary = ', required_necessary,
      '\nrequired_preffered = ', required_preffered,
      '\nwillPrint = ', willPrint,
      '\nwillScore = ', willScore,
      '\nfileType = ', "'%s'" %(fileType),
      '\nstartLog = ', startLog, 
      "\n\ninput '.' to keep the value already here.\n")

wrdLength = inter("wrdLength")
##addOne = inter("addOne")
##strictness = inter("strictness")
##input("letters = []
##input("repeats = []
##input("required = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}
required_necessary = bolea("required_necessary")
print(required_necessary)
if required_necessary:
    required_preffered = True
else:
    required_preffered = bolea("required_preffered")
willPrint = bolea("willPrint")
willScore = inter("willScore")

Type = input("fileType = ")
fileType = '%s' %(Type)
print(fileType)
startLog = bolea("startLog")

output = open("thisOutput.pyw", 'w')
print('wrdLength = ', wrdLength,
      '\naddOne = ', addOne,
      '\nstrictness = ', strictness,
      '\nletters = ', letters,
      '\nrepeats = ', repeats,
      '\nrequired = ', required,
      '\nrequired_necessary = ', required_necessary,
      '\nrequired_preffered = ', required_preffered,
      '\nwillPrint = ', willPrint,
      '\nwillScore = ', willScore,
      '\nfileType = ', "'%s'" %(fileType),
      '\nstartLog = ', startLog,
      sep='', file=output)

output.close()
