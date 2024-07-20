import random

def pattern(r, c): return (3*(r%3) + r//3 + c) % 9
def shuffle(s): return random.sample(s, len(s))

def generate_board():
    rBase = range(3)
    rows  = [ g*3 + r for g in shuffle(rBase) for r in shuffle(rBase) ]
    cols  = [ g*3 + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1, 10))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = 9*9
    empties = squares * 3//4
    for p in random.sample(range(squares), empties):
        board[p//9][p%9] = 0

    return board

def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - -")
        print(" ".join(str(val) if val != 0 else '.' for val in row[:3]), end=" | ")
        print(" ".join(str(val) if val != 0 else '.' for val in row[3:6]), end=" | ")
        print(" ".join(str(val) if val != 0 else '.' for val in row[6:]))

def solve(board):
    def is_valid(board, r, c, num):
        for i in range(9):
            if board[i][c] == num or board[r][i] == num:
                return False
        startRow, startCol = 3*(r//3), 3*(c//3)
        for i in range(3):
            for j in range(3):
                if board[i+startRow][j+startCol] == num:
                    return False
        return True

    def solve_board(board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            if solve_board(board):
                                return True
                            board[r][c] = 0
                    return False
        return True

    board_copy = [row[:] for row in board]
    solve_board(board_copy)
    return board_copy

def play_sudoku():
    board = generate_board()
    solved_board = solve(board)
    user_entries = [[False] * 9 for _ in range(9)]

    while True:
        print("\nCurrent Sudoku Board:")
        print_board(board)
        print("\nOptions: \n1. Fill a cell\n2. Show solution\n3. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                value = int(input("Enter value (1-9): "))
                if board[row][col] == 0 or user_entries[row][col]:
                    if solved_board[row][col] == value:
                        board[row][col] = value
                        user_entries[row][col] = True
                    else:
                        print("Incorrect value.")
                else:
                    print("This cell is part of the initial puzzle and cannot be changed.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except IndexError:
                print("Invalid input. Row and column must be between 1 and 9.")
        elif choice == '2':
            print("\nSolution:")
            print_board(solved_board)
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Please choose again.")

play_sudoku()
