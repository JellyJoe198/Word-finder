# Dictionary sorter
This program takes a dictionary and outputs words that fit certain criteria into a text file.  
Once cloned to your computer, edit `settings.py` (with IDLE or a plaintext editor) to change these parameters, then run `dictionary sorter.py` to sort them  
Version 0.6.4 has different variables but it has comments in the code to help.

### System Requirements
- python 3 (3.7 is what I am using but others should work)

## Variables  

__wrdLength:__  
This is the length of the words to output.  
__addOne:__  
This is the length more than wrdLength it will also output.  
__leniency:__  
How many incorrect letters are allowed? This is similar to blank tiles that can be any letter.  

__letters:__  
Use this like your tile rack, it is the list of letters that are free to go anywhere.  
Each letter will be used up to one time. To repeat, put a letter in multiple times.  
It is faster for common letters to be earlier but not required.  

__required:__  
Use this like the letters already on the board, the number is the place in the word where the letter must go.  
It skips the letters check so don't put these in `letters` _**note: this might change as it is clumsy**_  
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
