
## Make a UI
This could be a number of things, but it needs to be easy to use and easy to customize the search.

### vision
User tells the UI the tiles he has, then tells it the place on the board to which it has to fit. (places on board would loosely correspond to `required` variable) This method should make it easy for the user to see exactly how search will happen, and control what conditions it will use. There may also be variables outside of the board, possibly to control the style of the output or

### Requirements
* keyboard accessability (mouse is not necessary; keyboarders are not second class citizens)
* retain as much customization as possible, including dictionary
* complex board:
    - multi layered - you can apply filters to many different position, and it doesn't have to be the same filter everywhere. Possibly an automatic mode that would take the start of a word and return what can go there
    - you can test multiple positions on the board at the same time, and they wouldn't affect eachother
* awesomeness

### possible methods
Use an intermediate file to separate core from UI. This would allow many different versions of UI to seamlessly integrate without redoing the core, and edge cases are easier to diagnose bc sharing the file instead of UI screenshot. The intermediate file could even be a JSON file to make it compatible with more languages.
