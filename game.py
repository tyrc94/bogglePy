import random
import time
import os


def randomise_board():
    LETTERS = [
        ['A', 'A', 'C', 'I', 'O', 'T'],
        ['A', 'B', 'I', 'L', 'T', 'Y'],
        ["A", "B", "J", "M", "O", "Qu"],
        ["A", "C", "D", "E", "M", "P"],
        ["A", "C", "E", "L", "R", "S"],
        ["A", "D", "E", "N", "V", "Z"],
        ["A", "H", "M", "O", "R", "S"],
        ["B", "I", "F", "O", "R", "X"],
        ["D", "E", "N", "O", "S", "W"],
        ["D", "K", "N", "O", "T", "U"],
        ["E", "E", "F", "H", "I", "Y"],
        ["E", "G", "K", "L", "U", "Y"],
        ["E", "G", "I", "N", "T", "V"],
        ["E", "H", "I", "N", "P", "S"],
        ["E", "L", "P", "S", "T", "U"],
        ["G", "I", "L", "R", "U", "W"]
    ]

    board = [None for _ in range(len(LETTERS))]

    cubes = 0
    i = 0
    while cubes < 16:
        cube = LETTERS.pop(random.randint(0, len(LETTERS)-1))
        letter = cube[random.randint(0, len(cube)-1)]
        board[i] = letter
        i += 1
        cubes += 1

    board = [board[x:x+4] for x in range(0, 16, 4)]  # converts the board to a 2d array

    return board


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        t -= 1


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux (os.name is 'posix')
    else:
        _ = os.system('clear')


def main():
    #  Board creation
    board = randomise_board()

    #  Board display
    for x in range(4):
        for y in range(4):
            print('{}'.format(board[x][y]),  end="  " if board[x][y] != 'Qu' else " "),
        print()

    #  Countdown timer
    print("\nTime remaining:")
    countdown(180)  # 3 minute timer
    clear()  # Clears screen after time has elapsed

    print("Time's up!")


if __name__ == "__main__":
    main()
