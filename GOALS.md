
## Make a UI
This could be a number of things, but it needs to be easy to use and easy to customize the search.

### vision
In the UI you would tell it the tiles that you have, and then have environments on the board that it would put them in. (environments would loosely correspond to `required` variable as places on the board) This method would make it very easy for the user to see exactly how search will happen.

### Requirements
* keyboard accessability (mouse is not necessary; keyboarders are not second class citizens)
* retain as much customizing as possible, including:
    - dictionary
    - output style (including logs)

### possible methods
Use an intermediate file to separate core from UI. This would allow many different versions of UI to seamlessly integrate without redoing the core, and edge cases are easier to diagnose bc sharing the file instead of UI screenshot. The intermediate file could even be a JSON file to make it compatible with more languages.
