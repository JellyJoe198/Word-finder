# Dictionary sorter
once cloned to your computer, edit the file (with IDLE or other) to change the parameters.  
_note: I use a lot of scrabble/words with friends references here because that is what this was initially for._

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
There is a guide under the `letters` variable for convenience

__required:__  
Use this like the letters already on the board, the number is the place in the word where the letter must go.  
It skips the letters check so don't put these in `letters` _note: this might change as it is clumsy_  
You can also use an array if multiple letters can go in that place. example: `['s','y','e']`
Enter a `'0'` to ignore that slot.  
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


## Dictionary generator
The generator is based on a similar concept but it takes dictionaries and filters them based on certain criteria. I used it to generate the dictionary sorter uses. 
