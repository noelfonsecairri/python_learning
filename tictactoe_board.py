#position = input('enter number: ')

the_board = [' ', 'X', ' ', '|', ' ', 'X', ' ','|',' ', 'X', ' ', '\n', 
			 '_', '_', '_', '|', '_', '_', '_','|', '_', '_','_', '\n',
			 ' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', '\n', 
			 ' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', '\n', 
			 '_', '_', '_', '|', '_', '_', '_','|', '_', '_','_', '\n',
			 ' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', '\n', 
			 ' ', ' ', ' ', '|', ' ', ' ', ' ','|',' ', ' ', ' ', ]

the_board2 = [' ', 'X', ' ', '|', ' ', 'X', ' ', '|', ' ', 'X', ' ', '\n', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_', '\n', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\n', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\n', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_', '\n', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\n', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']

print(the_board == the_board2)



#print(the_board.index('a'))


print(the_board[1] == the_board[5] == the_board[9] == 'X' or the_board[1] == the_board[5] == the_board[9] == 'O' or the_board[37] == the_board[41] == the_board[45] == 'X' or the_board[37] == the_board[41] == the_board[45] == 'O' or the_board[73] == the_board[77] == the_board[81] == 'X' or the_board[73] == the_board[77] == the_board[81] == 'O' or the_board[1] == the_board[37] == the_board[73] == 'X' or the_board[1] == the_board[37] == the_board[73] == 'O' or the_board[5] == the_board[41] == the_board[77] == 'X' or the_board[5] == the_board[41] == the_board[77] == 'O' or the_board[9] == the_board[73] == the_board[81] == 'X' or the_board[9] == the_board[73] == the_board[81] == 'O' or the_board[1] == the_board[41] == the_board[81] == 'X' or the_board[1] == the_board[41] == the_board[81] == 'O' or the_board[9] == the_board[41] == the_board[73] == 'X' or the_board[9] == the_board[41] == the_board[73] == 'O')

print(''.join(the_board))
