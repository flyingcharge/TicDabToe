import sys
import random
import signal
import time
import copy

class TimedOutExc(Exception):
	pass

def handler(signum, frame):
	#print 'Signal handler called with signal', signum
	raise TimedOutExc()

class Random_Player():
	def __init__(self):
		pass

	def move(self, board, old_move, flag):
		#You have to implement the move function with the same signature as this
		#Find the list of valid cells allowed
		cells = board.find_valid_move_cells(old_move)
		return cells[random.randrange(len(cells))]


class player14:
	def __init__(self):
		pass

	def get_empty_cells(self, board, bla1):
		cells = [] #list of tuples that are allowed
		#Iterate over all the blocks that are possible, in this case it is only 1 and get all the empty cells

		for x in bla1:
			id1 = x/4
			id2 = x%4

			for i in xrange(id1*4, id1*4 + 4):
				for j in xrange(id2*4, id2*4 + 4):
					if board.board_status[i][j] == '-':
						cells.append((i,j))
		#Or else if all the blocks are full, move anywhere
		if cells == []:
			for i in range(16):
				for j in range(16):
					no = (i/4)*4 + j/4
					if board.board_status == '-' and board.block_status[no] == '-':
						cells.append((i,j))
		return cells

 
	def get_blocks(self, board, old_move):
		#Did not define for_corner variable, check later

		#list of permitted blocks, based on old move
		block_allowed = []

		#Omitting old moves of corners because we do not have 3 choices

		#We have only one block to choose from anyway, according to the rules

		#this is the first row.
		if old_move[0]%4==0:
			if old_move[1] in [1,5,9,13]:
				#BLOCK NUMBER 1 in diagram
				block_allowed=[1]
			
			elif old_move[1] in [0,4,8,12]:
				#0 number
				block_allowed=[0]
			elif old_move[1] in [2,6,10,14]:
				#2 number
				block_allowed=[2]
			elif old_move[1] in [3,7, 11,15]:
				#3 number
				block_allowed=[3]

		#This is the second row.
		elif old_move[0]%4==1:
			if old_move[1] in [0,4,8,12]:
				#BLOCK NUMBER 4 in diagram
				block_allowed=[4]
			
			elif old_move[1] in [1,5,9,13]:
				#5 number
				block_allowed=[5]
			elif old_move[1] in [2,6,10,14]:
				#6 number
				block_allowed=[6]
			elif old_move[1] in [3,7, 11,15]:
				#7 number
				block_allowed=[7]

		#This is row no. 3
		elif old_move[0]%4==2:
			if old_move[1] in [0,4,8,12]:
				#BLOCK NUMBER 8 in diagram
				block_allowed=[8]
			
			elif old_move[1] in [1,5,9,13]:
				#9 number
				block_allowed=[9]
			elif old_move[1] in [2,6,10,14]:
				#10 number
				block_allowed=[10]
			elif old_move[1] in [3,7, 11,15]:
				#11 number
				block_allowed=[11]

        #This is row no. 4
		elif old_move[0]%4==3:
			if old_move[1] in [0,4,8,12]:
				#BLOCK NUMBER 12 in diagram
				block_allowed=[12]
			
			elif old_move[1] in [1,5,9,13]:
				#13 number
				block_allowed=[13]
			elif old_move[1] in [2,6,10,14]:
				#14 number
				block_allowed=[14]
			elif old_move[1] in [3,7, 11,15]:
				#15 number
				block_allowed=[15]

		#Also if a block is already decided, we remove it from block_allowed
		for i in reversed(block_allowed):
			if board.board_status[i]!='-':
				block_allowed.remove(i)
			
		#return all the empty cells in the block allowed
		return self.get_empty_cells(board, block_allowed)

	def terminal_state_reached(self, board):
		#CHECK ROW WIN
		if (board.block_status[0]== board.block_status[1] and board.block_status[1]==board.block_status[2] and board.block_status[2]==board.block_status[3] and board.block_status[1]!='-' and board.block_status[1]!='d') or
		(board.block_status[4]== board.block_status[5] and board.block_status[5]==board.block_status[6] and board.block_status[6]==board.block_status[7] and board.block_status[4]!='-' and board.block_status[4]!='d') or
		(board.block_status[8]== board.block_status[9] and board.block_status[9]==board.block_status[10] and board.block_status[10]==board.block_status[11] and board.block_status[8]!='-' and board.block_status[8]!='d') or
		(board.block_status[12]== board.block_status[13] and board.block_status[13]==board.block_status[14] and board.block_status[14]==board.block_status[15] and board.block_status[12]!='-' and board.block_status[12]!='d'):
			return True, 'W'
		

		#Check col win
		elif (board.block_status[0]== board.block_status[4] and board.block_status[4]==board.block_status[8] and board.block_status[8]==board.block_status[12] and board.block_status[0]!='-' and board.block_status[0]!='d') or
		(board.block_status[1]== board.block_status[5] and board.block_status[5]==board.block_status[9] and board.block_status[9]==board.block_status[13] and board.block_status[1]!='-' and board.block_status[1]!='d') or
		(board.block_status[2]== board.block_status[6] and board.block_status[6]==board.block_status[10] and board.block_status[10]==board.block_status[14] and board.block_status[2]!='-' and board.block_status[2]!='d') or
		(board.block_status[3]== board.block_status[7] and board.block_status[7]==board.block_status[11] and board.block_status[11]==board.block_status[15] and board.block_status[3]!='-' and board.block_status[3]!='d'):
			return True, 'W'
		
		#Check diagonal win
		elif (board.block_status[0]== board.block_status[5] and board.block_status[5]==board.block_status[10] and board.block_status[10]==board.block_status[15] and board.block_status[0]!='-' and board.block_status[0]!='d') or
		(board.block_status[3]== board.block_status[6] and board.block_status[6]==board.block_status[9] and board.block_status[9]==board.block_status[12] and board.block_status[3]!='-' and board.block_status[3]!='d'):
			return True, 'W'
		
		else:
			smflag=0
			for i in xrange(9):
				for j in xrange(9):
					if board.board_status[i][j] == '-' and board.block_status[(i/4)*4 + (j/4)] == '-':
						smflag =1
						break
			
			if smflag == 1
			#GAME IS ON BRO
				return False, 'Continue'
			else:
				return False, 'Tie'


	def update_overall_board(self, board, move_ret, fl ):
		#check if we need to modify block_stat

		block_no = (move_ret[0]/4)*4 + move_ret[1]/4

		updated_block, id1,id2, mflg = -1, block_no/4, block_no%4, 0

		if board.block_status[block_no] == '-':
			if board.board_status[id1*4][id2*4] == board.board_status[id1*4+1][id2*4+1] and boad.board_status[id1*4+1][id2*4+1] == board.board_status[id1*4+2][id2*4+2] and board.board_status[id1*4+1][id2*4+1] != '-':
				mflg=1
			if board.board_status[id1*4+2][id2*4] == board.board_status[id1*4+1][id2*4+1] and board.board_status[id1*4+1][id2*4+1] == board.board_status[id1*4][id2*4+ 2] and board.board_status[id1*4+1][id2*4+1] != '-':
				mflg=1

		#colwise update
		if mflg !=1:
			for i in xrange(id2*4, id2*4 + 4):
				if board.board_status[]


	def alpha_beta_pruning(self, board, old_move, alpha, beta, flag , depth):
		if(depth ==  4)
			'''
				Heuristic
			'''
			return [old_move[0], old_move[1], self.Winning_Heuristic(board, flag)]


        coords = self.get_blocks(board, old_move)
		print "cell is "
		print coords

		if flag == 1:
			symbol = 'o'
		else
			symbol = 'x'

		if depth%2 == 0:
			''' Max Node '''

			max_list = [-1, -1 , -100000]
			for i in coords:
				a, b = i
				board.board_status[a][b] = symbol

				board.block_status , updated_block = self.update_overall_board(board,(a,b),symbol)
				game_state, message =  self.terminal_state_reached(board)

				if game_state:
					board.board_status[a][b]='-'
					if updated_block != -1:
						board.block_status[updated_block] = '-'
					return [a, b, 10000]

				val = self.alpha_beta_pruning(board, (a,b), alpha, beta, flag^1, depth+1)

				if(val[2] > max_list[2]):
					max_list[0], max_list[1], max_list[2] =a , b , val[2];
				
				alpha = max(alpha, max_list[2])
				board.board_status[a][b] = '-'

				if updated_block != -1:
					board.block_status[updated_block] = '-'
				
				if (beta <= alpha):
					break
			
			return max_list
		else:
			'''Min Node '''

			min_list = [-1, -1, 100000]
			for i in coords:
				a, b = i
			
				board.board_status[a][b] = symbol

				board.block_status , updated_block = self.update_overall_board(board,(a,b),symbol)
				game_state, message =  self.terminal_state_reached(board)

				if game_state:
					board.board_status[a][b]='-'
					if updated_block != -1:
						board.block_status[updated_block] = '-'
					return [a, b, -10000]

				val = self.alpha_beta_pruning(board, (a,b), alpha, beta, flag^1, depth+1)

				if(val[2] <= min_list[2]):
					min_list[0], min_list[1], min_list[2] =a , b , val[2];
				
				beta = min(beta, min_list[2])
				board.board_status[a][b] = '-'

				# STAAAAAAAR CHANGE, because this is list, and we have a 2d array
				
				if updated_block != -1:
					board.block_status[updated_block] = '-'
				
				if (beta <= alpha):
					break
			
			return min_list



	def move(self, board, old_move, flag):
		if flag == 'x':
			flag=1
		else:
			flag=0
	
	coord = tuple(self.alpha_beta_pruning(board, old_move, -10**6-1, 10**6, flag, 0)[0:2])
	
	#if old move is (-1,-1)
	if coord[0] == -1 or coord[0] == -1:
		coords = self.get_blocks(board, old_move)
		return coords[random.randrange(len(cells))]
	
	#return move
	return coord






class Manual_Player:
	def __init__(self):
		pass
	def move(self, board, old_move, flag):
		print 'Enter your move: <format:row column> (you\'re playing with', flag + ")"	
		mvp = raw_input()
		mvp = mvp.split()
		return (int(mvp[0]), int(mvp[1]))

class Board:

	def __init__(self):
		# board_status is the game board
		# block status shows which blocks have been won/drawn and by which player
		self.board_status = [['-' for i in range(16)] for j in range(16)] #BIIIG BAORD
		self.block_status = [['-' for i in range(4)] for j in range(4)]  #SAME FOR BOTH CODES

	def print_board(self):
		# for printing the state of the board
		print '==============Board State=============='
		for i in range(16):
			if i%4 == 0:
				print
			for j in range(16):
				if j%4 == 0:
					print "",
				print self.board_status[i][j],
			print 
		print

		print '==============Block State=============='
		for i in range(4):  #printing horizontally
			for j in range(4):
				print self.block_status[i][j],
			print 
		print '======================================='
		print
		print


	def find_valid_move_cells(self, old_move):
		#returns the valid cells allowed given the last move and the current board state
		allowed_cells = []
		allowed_block = [old_move[0]%4, old_move[1]%4]
		#checks if the move is a free move or not based on the rules

		if old_move != (-1,-1) and self.block_status[allowed_block[0]][allowed_block[1]] == '-':
			for i in range(4*allowed_block[0], 4*allowed_block[0]+4):
				for j in range(4*allowed_block[1], 4*allowed_block[1]+4):
					if self.board_status[i][j] == '-':
						allowed_cells.append((i,j))
		else:
			for i in range(16):
				for j in range(16):
					if self.board_status[i][j] == '-' and self.block_status[i/4][j/4] == '-':
						allowed_cells.append((i,j))
		return allowed_cells	

	def find_terminal_state(self):
		#checks if the game is over(won or drawn) and returns the player who have won the game or the player who has higher blocks in case of a draw
		bs = self.block_status

		cntx = 0
		cnto = 0
		cntd = 0

		for i in range(4):						#counts the blocks won by x, o and drawn blocks
			for j in range(4):
				if bs[i][j] == 'x':
					cntx += 1
				if bs[i][j] == 'o':
					cnto += 1
				if bs[i][j] == 'd':
					cntd += 1

		for i in range(4):
			row = bs[i]							#i'th row 
			col = [x[i] for x in bs]			#i'th column
			#print row,col
			#checking if i'th row or i'th column has been won or not
			if (row[0] =='x' or row[0] == 'o') and (row.count(row[0]) == 4):	
				return (row[0],'WON')
			if (col[0] =='x' or col[0] == 'o') and (col.count(col[0]) == 4):
				return (col[0],'WON')
		#checking if diagnols have been won or not
		if(bs[0][0] == bs[1][1] == bs[2][2] ==bs[3][3]) and (bs[0][0] == 'x' or bs[0][0] == 'o'):
			return (bs[0][0],'WON')
		if(bs[0][3] == bs[1][2] == bs[2][1] ==bs[3][0]) and (bs[0][3] == 'x' or bs[0][3] == 'o'):
			return (bs[0][3],'WON')

		if cntx+cnto+cntd <16:		#if all blocks have not yet been won, continue
			return ('CONTINUE', '-')
		elif cntx+cnto+cntd == 16:							#if game is drawn
			return ('NONE', 'DRAW')

	def check_valid_move(self, old_move, new_move):
		#checks if a move is valid or not given the last move
		if (len(old_move) != 2) or (len(new_move) != 2):
			return False 
		if (type(old_move[0]) is not int) or (type(old_move[1]) is not int) or (type(new_move[0]) is not int) or (type(new_move[1]) is not int):
			return False
		if (old_move != (-1,-1)) and (old_move[0] < 0 or old_move[0] > 16 or old_move[1] < 0 or old_move[1] > 16):
			return False
		cells = self.find_valid_move_cells(old_move)
		return new_move in cells

	def update(self, old_move, new_move, ply):
		#updating the game board and block status as per the move that has been passed in the arguements
		if(self.check_valid_move(old_move, new_move)) == False:
			return 'UNSUCCESSFUL'
		self.board_status[new_move[0]][new_move[1]] = ply

		x = new_move[0]/4
		y = new_move[1]/4
		fl = 0
		bs = self.board_status
		#checking if a block has been won or drawn or not after the current move
		for i in range(4):
			#checking for horizontal pattern(i'th row)
			if (bs[4*x+i][4*y] == bs[4*x+i][4*y+1] == bs[4*x+i][4*y+2] == bs[4*x+i][4*y+3]) and (bs[4*x+i][4*y] == ply):
				self.block_status[x][y] = ply
				return 'SUCCESSFUL'
			#checking for vertical pattern(i'th column)
			if (bs[4*x][4*y+i] == bs[4*x+1][4*y+i] == bs[4*x+2][4*y+i] == bs[4*x+3][4*y+i]) and (bs[4*x][4*y+i] == ply):
				self.block_status[x][y] = ply
				return 'SUCCESSFUL'

		#checking for diagnol pattern
		if (bs[4*x][4*y] == bs[4*x+1][4*y+1] == bs[4*x+2][4*y+2] == bs[4*x+3][4*y+3]) and (bs[4*x][4*y] == ply):
			self.block_status[x][y] = ply
			return 'SUCCESSFUL'
		if (bs[4*x+3][4*y] == bs[4*x+2][4*y+1] == bs[4*x+1][4*y+2] == bs[4*x][4*y+3]) and (bs[4*x+3][4*y] == ply):
			self.block_status[x][y] = ply
			return 'SUCCESSFUL'

		#checking if a block has any more cells left or has it been drawn
		for i in range(4):
			for j in range(4):
				if bs[4*x+i][4*y+j] =='-':
					return 'SUCCESSFUL'
		self.block_status[x][y] = 'd'
		return 'SUCCESSFUL'

def gameplay(obj1, obj2):				#game simulator

	game_board = Board() #Equivalent: 	game_board, block_stat = get_init_board_and_blockstatus()

	fl1 = 'x'
	fl2 = 'o'
	old_move = (-1,-1)
	WINNER = ''
	MESSAGE = ''
	TIME = 15
	pts1 = 0
	pts2 = 0

	game_board.print_board()
	signal.signal(signal.SIGALRM, handler)
	while(1):
		#player 1 turn
		temp_board_status = copy.deepcopy(game_board.board_status)
		temp_block_status = copy.deepcopy(game_board.block_status)
		signal.alarm(TIME)

		try:									#try to get player 1's move			
			p1_move = obj1.move(game_board, old_move, fl1)
		except TimedOutExc:					#timeout error
#			print e
			WINNER = 'P2'
			MESSAGE = 'TIME OUT'
			pts2 = 16
			break
		except Exception as e:
			WINNER = 'P2'
			MESSAGE = 'INVALID MOVE'
			pts2 = 16			
			break
		signal.alarm(0)

		#check if board is not modified and move returned is valid
		if (game_board.block_status != temp_block_status) or (game_board.board_status != temp_board_status):
			WINNER = 'P2'
			MESSAGE = 'MODIFIED THE BOARD'
			pts2 = 16
			break
		if game_board.update(old_move, p1_move, fl1) == 'UNSUCCESSFUL':
			WINNER = 'P2'
			MESSAGE = 'INVALID MOVE'
			pts2 = 16
			break

		status = game_board.find_terminal_state()		#find if the game has ended and if yes, find the winner
		print status
		if status[1] == 'WON':							#if the game has ended after a player1 move, player 1 would win
			pts1 = 16
			WINNER = 'P1'
			MESSAGE = 'WON'
			break
		elif status[1] == 'DRAW':						#in case of a draw, each player gets points equal to the number of blocks won
			WINNER = 'NONE'
			MESSAGE = 'DRAW'
			break

		old_move = p1_move
		game_board.print_board()

		#do the same thing for player 2
		temp_board_status = copy.deepcopy(game_board.board_status)
		temp_block_status = copy.deepcopy(game_board.block_status)
		signal.alarm(TIME)

		try:
			p2_move = obj2.move(game_board, old_move, fl2)
		except TimedOutExc:
			WINNER = 'P1'
			MESSAGE = 'TIME OUT'
			pts1 = 16
			break
		except Exception as e:
			WINNER = 'P1'
			MESSAGE = 'INVALID MOVE'
			pts1 = 16			
			break
		signal.alarm(0)
		if (game_board.block_status != temp_block_status) or (game_board.board_status != temp_board_status):
			WINNER = 'P1'
			MESSAGE = 'MODIFIED THE BOARD'
			pts1 = 16
			break
		if game_board.update(old_move, p2_move, fl2) == 'UNSUCCESSFUL':
			WINNER = 'P1'
			MESSAGE = 'INVALID MOVE'
			pts1 = 16
			break

		status = game_board.find_terminal_state()	#find if the game has ended and if yes, find the winner
		print status
		if status[1] == 'WON':						#if the game has ended after a player move, player 2 would win
			pts2 = 16
			WINNER = 'P2'
			MESSAGE = 'WON'
			break
		elif status[1] == 'DRAW':					
			WINNER = 'NONE'
			MESSAGE = 'DRAW'
			break
		game_board.print_board()
		old_move = p2_move

	game_board.print_board()

	print "Winner:", WINNER
	print "Message", MESSAGE

	x = 0
	d = 0
	o = 0
	for i in range(4):
		for j in range(4):
			if game_board.block_status[i][j] == 'x':
				x += 1
			if game_board.block_status[i][j] == 'o':
				o += 1
			if game_board.block_status[i][j] == 'd':
				d += 1
	print 'x:', x, ' o:',o,' d:',d
	if MESSAGE == 'DRAW':
		pts1 = x
		pts2 = o
	return (pts1,pts2)



if __name__ == '__main__':

	if len(sys.argv) != 2:
		print 'Usage: python simulator.py <option>'
		print '<option> can be 1 => Random player vs. Random player'
		print '                2 => Human vs. Random Player'
		print '                3 => Human vs. Human'
		sys.exit(1)
 
	obj1 = ''
	obj2 = ''
	option = sys.argv[1]	
	if option == '1':
		obj1 = Random_Player()
		obj2 = Random_Player()

	elif option == '2':
		obj1 = Random_Player()
		obj2 = Manual_Player()
	elif option == '3':
		obj1 = Manual_Player()
		obj2 = Manual_Player()
	else:
		print 'Invalid option'
		sys.exit(1)

	x = gameplay(obj1, obj2)
	print "Player 1 points:", x[0] 
	print "Player 2 points:", x[1]
