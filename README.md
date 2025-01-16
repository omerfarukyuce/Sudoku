# 🧩 Sudoku Game

This project is a Python application that allows users to play Sudoku. The application generates a random Sudoku board and provides options for users to fill in the board or view the solution.

## 🚀 Features

- **Random Sudoku Board Generation:** The application creates a new Sudoku puzzle each time it is run.
- **User Input:** Users can fill in cells with numbers from 1 to 9.
- **Solution Display:** Users can view the complete solution of the Sudoku puzzle.
- **Input Validation:** The application checks for valid inputs and provides feedback for incorrect entries.

## 📦 Requirements

- Python 3.x
- The `random` module (comes pre-installed with Python)

## 🎮 How to Play

1. **Fill a Cell:** Choose the option to fill a cell. You will be prompted to enter the row (1-9), column (1-9), and the value (1-9) you want to place in that cell.
2. **Show Solution:** If you want to see the solution to the Sudoku puzzle, select this option.
3. **Quit:** Exit the game.

### 🎯 Input Instructions

- When prompted to fill a cell, ensure that:
  - The row and column numbers are between 1 and 9.
  - The value you enter is between 1 and 9.
- If you attempt to change a cell that is part of the initial puzzle, the application will notify you that it cannot be changed.

## 🎮 Example Gameplay

1. Start the game by running `python sudoku.py`.
2. Follow the on-screen instructions to fill in the Sudoku board.
3. Use the option to show the solution if you need help.


## 📝 License

This project is licensed under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file.
