
# Square Shell Matrix Generator

## Overview
The **Square Shell Matrix Generator** creates an \( n 	imes n \) matrix filled with numbers in ascending order, starting from the outermost layer and moving inward in a clockwise direction. The size of the matrix is provided by the user at runtime.

## Problem Statement
Write a Python program that generates a matrix with numbers in ascending order, arranged in a square shell pattern. The program should:
- Take a single input: the **length of the side** of the matrix.
- Print the matrix in a square shell (spiral) order.

### Example
For a matrix with a side length of 5, the output should be:
```
00 01 02 03 04
15 16 17 18 05
14 23 24 19 06
13 22 21 20 07
12 11 10 09 08
```

## Time and Space Complexity
- **Time Complexity**: \( O(n^2) \)
  - The algorithm iterates through all \( n^2 \) elements in the matrix to fill them in spiral order.
- **Space Complexity**: \( O(n^2) \)
  - The matrix itself requires space to store \( n^2 \) elements.

## Example Usage
When you run the script:
```
$ python spiral_matrix.py
Enter the size of the square matrix (positive integer): 5
00 01 02 03 04
15 16 17 18 05
14 23 24 19 06
13 22 21 20 07
12 11 10 09 08
```

### Output for the Example
If you enter `5` as the matrix size, the program outputs:
```
00 01 02 03 04
15 16 17 18 05
14 23 24 19 06
13 22 21 20 07
12 11 10 09 08
```

