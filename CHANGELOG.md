
# dictionary sorter change log

### 0.7.0
- you can now input repeatable letters just by putting more than 1 of that letter in the `letters` array, and it will only repeat the amount of times you put in that letter.

#### UI-text 0.1 - 0.6.5
- this is a text based user interface to make a settings file for dictionary sorter version 0.6.5. It is probably still better to directly edit settings.pyw though.

### 0.6.5
- dictionary sorter now uses an external file (currently settings.pyw) for the settings. This is so another program (not implemented yet) can change the settings file to communicate with it without changing it. I might find that there is a better way to do this later.

### 0.6.4
- setting fileType to `'null'` will disable outputting to a file (minor bug: will still create file but it is empty)
- option to put the settings used at the top of each Output. This is foundation for the ability to import settings from a file.

### 0.6.3
- you can now print the score to Output in csv format
- the strictness will now be adjusted for the word length where relevant
#### 0.6.3a
- minor usability improvement: unused `required` is now just `''` an empty string

### 0.6.2
- you can use required_necessary and required_preffered to make the program always use `required`, check `required` first then `letters` if not found, or not check `required` at all. 
- you can now disable printing the words (_it would only write to Output.txt_)
- score calculation can now be turned off

### 0.6.1
- ability to make other letters not fill the specified letter's spot (bug: this only partially works)
- ability to make multiple certain letters able to fill the same required spot

### 0.6.0
- you can specify where a letter has to go
- more speed optimization
