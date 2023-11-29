# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


import random
import csv
class Game:
    def __init__(self, player1, player2):
        self.board = [[None, None, None] for _ in range(3)]
        self.current_player = player1
        self.other_player = player2
        self.move_count = 0

    def play_turn(self):
        x, y = self.current_player.get_move(self.board)
        self.board[x][y] = self.current_player.symbol
        self.move_count += 1
        self.current_player, self.other_player = self.other_player, self.current_player

    def get_winner(self):

            for row in self.board:
                if row[0] == row[1] == row[2] and row[0] is not None:
                    return row[0]

            for i in range(3):
                if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                    return self.board[0][i]

            if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
                return self.board[0][0]
            if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
                return self.board[0][2]

            return None

    def is_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)
    
    def record_game_data(self, winner, mode):
        # Create the 'logs' directory if it doesn't exist

        # Open the file for appending
        with open('game_log.csv', "a") as f:
            
            f.write(f"{winner},{mode},{self.move_count}\n")


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        x, y = map(int, input(f"Enter the position of (x,y) for {self.symbol}, split with comma: ").split(","))
        return x, y

class Bot(Player):
    def get_move(self, board):
        # Simple bot logic: choose a random empty spot
        empty_spots = [(x, y) for x in range(3) for y in range(3) if board[x][y] is None]
        return random.choice(empty_spots) if empty_spots else (0, 0)
