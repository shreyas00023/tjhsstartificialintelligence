from Server import *
game = TicTacToe()
while(game.notover()):
    if game.winner('X'):
        print("You Won!")
        print(game)
        print()
        break
    if game.winner('O'):
        print("You Lost!")
        print(game)
        print()
        break
    print(game)
    row = int(input("Enter row: "))-1
    col = int(input("Enter col: "))-1
    while game.state[row][col] != None:
        row = int(input("Invalid, Enter row"))-1
        col = int(input("Invalid, Enter col"))-1
    print()
    game.post_move(row, col)
    move = game.get_move()
print("Game Over")


