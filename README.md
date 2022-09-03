Solve a Calcudoku.

First step is to make a simple text file with the calcudoku challenge in it.
The format is like this:

31+31+31+5+2-2-

20*31+31+5+3%3%

20*31+31+11+11+960*

3*3*12+11+11+960*

3*12+12+14+14+960*

6*6*6*14+960*960*


Store this file in the subfolder "input", or change the PATH in the code.
Use readpuzzel.py to automatically find the "calculation blocks".
The output can be found in "puzzels".
Check if the puzzel is correct. Problem is that the "calculation blocks" are of random form,
unlike the normal sudoku, that usually has fixed blocks of 3x3.

Use calcudoku.py to find the solution.

Have fun!
