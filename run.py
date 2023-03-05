from random import randint

score = {"computer": 0, "player": 0}


class Board:
    pass


class GameBoard:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        """ Method to print board """
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return 'Hit'
        else:
            return 'Miss'


    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):

    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    return None

def populate_board(board):
    for i in range(board.num_ships):
        x = randint(0, board.size - 1)
        y = randint(0, board.size - 1)
        if (x, y) not in board.ships:
            board.add_ship(x, y, board.type)


# def make_guess(board):

def play_game(computer_board, player_board):
    print("Computer board:")
    print(computer_board)
    print("Player board:")
    print(player_board)

    current_turn = "player"
    if current_turn == "player":
        current_turn = "computer"
    else:
        current_turn = "player"


def new_game():

    size = 5
    num_ships = 4
    score["computer"] = 0
    score["player"] = 0
    print("-" * 35)
    print("Welcome to title of game!")
    print(f"Board Size:{size},Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Enter your name here: \n")
    while len(player_name) == 0:
        print("invalid name")
        player_name = input("Enter your name here: \n")
    print("-" * 35)

    computer_board = GameBoard(size, num_ships, "Computer", type="computer")
    player_board = GameBoard(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

        play_game(computer_board, player_board)


new_game()
