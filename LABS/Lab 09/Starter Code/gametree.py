# Here is the board class; it has two attributes, knight and pawns; each piece is a pair of numbers between 0 and 7
class Board:
	def __init__(self, pieces):
		self.knight = pieces[0]
		self.pawns = pieces[1:]

	# prints board as 8 strings, 1 per line, with optional heading
	def printBoard(self, heading=""):
		if (heading):
			print(heading)
		board = [" - - - - - - - -"]*8
		(x,y) = self.knight
		row = board[x]
		board[x] = row[0:2*y+1] + "X" + row[2*y+2:]
		for (x,y) in self.pawns:
			row = board[x]
			board[x] = row[0:2*y+1] + "o" + row[2*y+2:]
		for row in board[:]:
			print(row)

	# returns list of knight moves that will eat a pawn, if any
	def findGoodMoves(self):
		(x0, y0) = self.knight
		moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
		goodMoves = []
		for (x, y) in moves:
			(x1, y1) = (x0 + x, y0 + y)
			#print ("trying move ", x, y)
			if (x1, y1) in self.pawns:
				goodMoves += [(x, y)]
		return goodMoves

	# returns a new board that's a copy of this one
	def copyBoard(self):
		newBoard = Board([self.knight]+self.pawns)
		return newBoard

	#given a board and a move, compute the next board
	def applyMove(self, move):
		(x0, y0) = self.knight
		(x, y) = move
		if (x0 + x) >= 0 and (y0 + y) >= 0:
			self.knight = (x0 + x, y0 + y)
			if self.knight in self.pawns:
				self.pawns.remove(self.knight)
			return True
		else:
			return False

	## Part 1
	def inverse(self, move):
		(x, y) = move
		move = (x*-1, y*-1)
		return move 

	def printGoodMovesBoard(self):
		goodMoves = self.findGoodMoves()
		self.printBoard("New Board")
		for move in goodMoves:
			#original = self
			self.applyMove(move)
			self.printBoard("Board with move " + str(move))
			self.applyMove(self.inverse(move))

	def printAllMovesBoard(self):
		pass


#---------------------------
bb = Board([(1,1), (3,2), (5,3), (0,3)])
#bb.printBoard("New board")
#print(bb.findGoodMoves())
#print(bb.applyMove((2,1)))
#bb.printBoard("New board")
bb.printGoodMovesBoard()