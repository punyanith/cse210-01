"""

Assignment: Tic-Tac-Toe
Author: Punyanith Tangsiriruangrit

"""

def main():
    grid = make_board()
    player = player_turn("")
    while not (current_game(grid)):
        show_grid(grid)
        start_game(player, grid)
        player = player_turn(player)
    show_grid(grid)
    print("Thank you for playing~")
    
def make_board():
    grid = []
    for row in range(9):
        grid.append(row + 1)
    return grid

def show_grid(grid):
    print()
    print(f" {grid[0]} | {grid[1]} | {grid[2]}")
    print("---+---+---")
    print(f" {grid[3]} | {grid[4]} | {grid[5]}")
    print("---+---+---")
    print(f" {grid[6]} | {grid[7]} | {grid[8]}")
    print()

def start_game(player, grid):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    grid[square - 1] = player

def current_game(grid):
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])

def player_turn(turn):

    if turn == "" or turn == "♥":
        return "*"
    elif turn == "*":
        return "♥"

if __name__=="__main__":
    main()