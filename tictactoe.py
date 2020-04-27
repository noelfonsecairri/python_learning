player1 = input("Please pick a marker 'X' or 'O': ").upper()
player2 = ''

while player1 not in ['X', 'O']:
	player1 = input("Please enter only 'X' or 'O'. ").upper()
else:
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'

print('Player 1 is: ' + player1)
print('Player 2 is: ' + player2)

player_x = input('Which player goes first? choose 1 for Player 1, and 2 for Player 2: ')

def player_one_or_two(player):
	while player not in ['1', '2']:
		player = input("Please only enter '1' or '2'.")
	else:
		if player == '1':
			return player1
		else:
			return player2

active_player = player_one_or_two(player_x)


def assign_board(new_board):
	the_board = new_board


the_board = [' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', '\n', 
			 '_', '_', '_', '|', '_', '_', '_','|', '_', '_','_', '\n',
			 ' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', '\n', 
			 ' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', '\n', 
			 '_', '_', '_', '|', '_', '_', '_','|', '_', '_','_', '\n',
			 ' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', '\n', 
			 ' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', ]


def print_board(board):
	board = ''.join(board)
	print(board)



def player_move(active_player, position, the_board):
	if active_player == player1:
		print('Player1 move: ')
	else:
		print('Player2 move: ')
	put_on_board(the_board, position, active_player)
	return the_board

winner = False
while winner != True:
 

	position = input('Please choose 1-9 as position: ')


	nums = list(range(1,10))
	def put_on_board(board, player_position, player):
		for num in nums:
			if position == str(nums[0]):
				the_board[1] = player
			elif position == str(nums[1]):
				the_board[5] = player
			elif position == str(nums[2]):
				the_board[9] = player
			elif position == str(nums[3]):
				the_board[37] = player
			elif position == str(nums[4]):
				the_board[41] = player
			elif position == str(nums[5]):
				the_board[45] = player
			elif position == str(nums[6]):
				the_board[73] = player
			elif position == str(nums[7]):
				the_board[77] = player
			elif position == str(nums[8]):
				the_board[81] = player

	board_is_taken = the_board[1] == 'X' or the_board[1] == 'O' or the_board[5] == 'X' or the_board[5] == 'O' or the_board[9] == 'X' or the_board[9] == 'O' or the_board[37] == 'X' or the_board[37] == 'O' or the_board[41] == 'X' or the_board[41] == 'O' or the_board[45] == 'X' or the_board[45] == 'O' or the_board[73] == 'X' or the_board[73] == 'O' or the_board[77] == 'X' or the_board[77] == 'O' or the_board[81] == 'X' or the_board[81] == 'O'

	winner_condition = the_board[1] == the_board[5] == the_board[9] == 'X' or the_board[1] == the_board[5] == the_board[9] == 'O' or the_board[37] == the_board[41] == the_board[45] == 'X' or the_board[37] == the_board[41] == the_board[45] == 'O' or the_board[73] == the_board[77] == the_board[81] == 'X' or the_board[73] == the_board[77] == the_board[81] == 'O' or the_board[1] == the_board[37] == the_board[73] == 'X' or the_board[1] == the_board[37] == the_board[73] == 'O' or the_board[5] == the_board[41] == the_board[77] == 'X' or the_board[5] == the_board[41] == the_board[77] == 'O' or the_board[9] == the_board[73] == the_board[81] == 'X' or the_board[9] == the_board[73] == the_board[81] == 'O' or the_board[1] == the_board[41] == the_board[81] == 'X' or the_board[1] == the_board[41] == the_board[81] == 'O' or the_board[9] == the_board[41] == the_board[73] == 'X' or the_board[9] == the_board[41] == the_board[73] == 'O'

	winner = winner_condition

	if active_player == player1:
		the_board = player_move(active_player, position, the_board)
		# winner = winner_condition
		active_player = player2
		print('Player 2 turn')
		
		

	elif active_player == player2:
		the_board = player_move(active_player, position, the_board)
		# winner = winner_condition
		active_player = player1
		print('Player 1 turn')
		
		

	if winner == True:
		print('Player ' + active_player + ' is the winner!')
		break
	
	print_board(the_board)
		



