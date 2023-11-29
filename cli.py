# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game, Player, Bot
import os
def print_board(board):
    for i, row in enumerate(board):
        print_row = [' ' if cell is None else cell for cell in row]
        print(' | '.join(print_row))
        if i < 2:
            print('---+---+---')
def main():
    mode = input("Choose mode (1 for single player, 2 for two players): ")
    player1 = Player('X')
    player2 = Bot('O') if mode == '1' else Player('O')

    game = Game(player1, player2)
    if not os.path.exists("game_log.csv"):
        with open("game_log.csv",'w') as f:
            f.write(f"winner, mode, move_count\n")
    while True:
        print_board(game.board)
        game.play_turn()
        winner = game.get_winner()
        if winner:
            print_board(game.board)
            print(f"Player {winner} wins!")
            game.record_game_data(winner,mode)
            break
        if game.is_draw():
            print_board(game.board)
            print("It's a draw!")
            game.record_game_data(winner,mode)
            break

if __name__ == '__main__':
    main()