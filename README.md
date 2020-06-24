# Dictionary sorter
This program takes a dictionary and outputs words that fit that criteria into a text file.  
Once cloned to your computer, edit the settings file (with IDLE or other) to change these parameters.  
Or you can use version 0.6.4 and edit the settings directly. (this may be better for now because`settings.pyw`has no guides)

__wrdLength:__  
This is the length of the words to output.  
__addOne:__  
This is the length more than wrdLength it will also output.  
__strictness:__  
The amount of correct letters required to output.  Should be `wrdLength` minus the amount of blank tiles.

__letters:__  
Use this like your tile rack, it is the list of letters that are free to go anywhere.  
It is good for common letters to be earlier but not required.  
Only 1 of each letter should be entered, if there are repeats use `repeats` variable.  
__repeats:__  
Put the location of the letter(s) that can repeat here, starting at 0.
In 0.6.4 there is a guide under the `letters` variable for convenience

__required:__  
Use this like the letters already on the board, the number is the place in the word where the letter must go.  
It skips the letters check so don't put these in `letters` _note: this might change as it is clumsy_  
You can also use an array if multiple letters can go in that place. example: `['s','y','e']`
Enter a blank string`''` to ignore that slot.  
__required_necessary:__  
True if other letters cannot fill the spots in `required`. False if stuff from `letters` can go in.  
__required_preffered:__  
True if it will check `required` before checking `letters`.  
Set both `required_necessary` and `required_preffered` to False to disable this check.  

__willPrint:__  
If False the program will not print the results to console, only Output (this makes it faster)  
__willScore:__  
If 0 the program will not calculate or print the score (this makes it slightly faster)  
If 1 the program will print score to console but not Output  
If 2 the program will print score to both console and Output  
__fileType:__  
The file extension that the output will be. ('csv' reccomended if you want scores, otherwise use 'txt')  
make it 'null' or 'pyw' to not output words (it will still output the settings if startLog is True)

__startLog:__  
True to print the settings used on that run at the start of each Output file

## Dictionary generator
The generator is based on a similar concept but it takes dictionaries and filters them based on certain criteria. I used it to generate the dictionary that the sorter uses. 
