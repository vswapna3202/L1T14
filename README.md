## L1T14: Data Structures: 2D Lists ##
This program when input with a mine and empty grid values as a grid-matrix displays an output of number of mines adjacent to each grid position as follows:
    - Creates a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot.
    - Returns a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally)

**Example Input:**
```
[ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]
```
**Example output:**
```
[ ["1", "1", "2", "#", "#"],
["1", "#", "3", "3", "2"],
["2", "4", "#", "2", "0"],
["1", "#", "#", "2", "0"],
["1", "2", "2", "1", "0"] ]
```
## Installation
1. **Python**: Ensure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/).
2. **Version**: These programs are written in Python 3. Make sure you have Python 3.x installed.

### Clone the Repository
```bash
git clone https://github.com/vswapna3202/L1T14.git  
```

## Running the programs <br>
Navigate to the directory of each Python file
Run Python using python interpreter
```
python minesweeper.py
