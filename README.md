# sudoku-solver
python code for a sudoku solver

## Motivation
I was needing to brush up on my Python coding since I have been focusing on R coding much more recently.
Additionally, I have had an idea for a solver for a long time. 

## Description
This rules based solver does not use any linear algebra to find solutions to 9x9 sudoku puzzles (My original idea did use linear algebra, but I quickly realized that it would not work very well.)
The input for the pogram consists of  "."s and the digits 1-9. "."s represent an empty square and a digit is for a square with a given entry.
The program first parses the input into 3 parallel lists each of length 81, (9x9). The parsing assigns the numbers possible for each one of the 81 squares in the grid.
Using this as input, the program then eliminates all impossible numbers from each entry based on what is in its row, column , and unit (1 3x3 block). This is looped until no more changes are made by the eliminate function.
The eliminated data is then fed into a selecting function that, for each row, column, and unit, selects out any values occuing only once and assigns them to the square they came from. This is done once.
If no changes are made then the program exits and prints its guess, otherwise the loop is started again, elimination followed by selection.

##Disclaimer
This is not guarrenteed to solve every Sudoku puzzle. Most easy puzzles can be done, but almost no hard puzzles can be solved.

