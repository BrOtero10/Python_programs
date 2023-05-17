import random

def rannum():
    numero_aleatorio = random.randint(1, 9)
    return numero_aleatorio

def row_cow():
    retorno = random.randint(0, 2)
    return retorno

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    coordinates = {
        1 : (0, 0),
        2 : (0, 1),
        3 : (0, 2),
        4 : (1, 0),
        5 : (1, 1),
        6 : (1, 2),
        7 : (2, 0),
        8 : (2, 1),
        9 : (2, 2)
    }

    move = int(input("Enter your move: "))

    if move not in coordinates:
        move = int(input("Enter a valid move: "))

    else:

        while board[coordinates[move[0]]][coordinates[move[1]]] == 'X' or board[coordinates[move[0]]][coordinates[move[1]]] == 'O':
            move = int(input("Enter a valid move: "))

        if board[coordinates[move[0]]][coordinates[move[1]]] != 'X' or board[coordinates[move[0]]][coordinates[move[1]]] != 'O':
            board[coordinates[move[0]]][coordinates[move[1]]] = "O"


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
    ]


def victory_for(board, sign = 'X'):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2] == sign:
            if sign == 'X':
                print("Computer wins!")
                return False

            elif sign == 'O':
                print("You won!")
                return False

        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] == sign:
                if sign == 'X':
                    print("Computer wins!")
                    return False

                elif sign == 'O':
                    print("You won!")
                    return False

    if board[0][0] == board[2][2] and board[2][2] == 'X':
        print("Computer wins!")
        return False

    if board[0][2] == board[2][0] and board[2][0] == 'X':
        print("Computer wins!")
        return False

    return True

def draw_move(board):

    if board[1][1] == '5':
        board[1][1] = 'X'
        return

    else:

        row = row_cow()
        cow = row_cow()
        
        while board[row][cow] == 'X' or board[row][cow] == 'O':
             row = row_cow()
             cow = row_cow()

             
        board[row][cow] = 'X'
        
        return 


board = [['0' for i in range(3)] for j in range(3)]

make_list_of_free_fields(board)
display_board(board)

while victory_for(board):

    enter_move(board)
    display_board(board)
    
    if victory_for(board, 'O'):
        break
        
    draw_move(board)
    display_board(board)
