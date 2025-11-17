def create_board():
return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
for row in board:
print(' | '.join(row))
print('-' * 5)

def is_valid_move(board, row, col):
return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, row, col, player):
if is_valid_move(board, row, col):
board[row][col] = player
return True
return False

def check_winner(board, player):

for row in board:
if all(cell == player for cell in row):
return True


for col in range(3):
if all(board[row][col] == player for row in range(3)):
return True


if all(board[i][i] == player for i in range(3)):
return True
if all(board[i][2 - i] == player for i in range(3)):
return True

return False

def is_draw(board):
return all(cell != ' ' for row in board for cell in row)

def play_game():
board = create_board()
current_player = 'X'

while True:
display_board(board)
print(f"Player {current_player}'s turn")

try:
row = int(input("Enter row (0-2): "))
col = int(input("Enter col (0-2): "))
except ValueError:
print("Invalid input! Please enter numbers 0, 1, or 2.")
continue

if make_move(board, row, col, current_player):
if check_winner(board, current_player):
display_board(board)
print(f"🎉 Player {current_player} wins!")
break
elif is_draw(board):
display_board(board)
print("It's a draw!")
break
current_player = 'O' if current_player == 'X' else 'X'
else:
print("Invalid move! Try again.")

if __name__ == "__main__":
play_game()
