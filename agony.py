import os.path
import sys
from Board import PieceColor, Board, transform_coords, interpret_coords, out_of_bounds
from referee.Game import Game
import time
import copy

depth = 0
maxPlayer = True
bestMove = []
ourPlayer = PieceColor.NONE


def min_max_algo(board: Board, color: PieceColor, depth: int, goalDepth: int, maxPlayer: bool, Ocolor: PieceColor, alpha: int, beta: int) -> float:
   global bestMove
   if maxPlayer:
       maxValue = -999999
       listOfMoves = get_valid_moves(board, color)
       if depth == goalDepth:
           return eval_func(board, color)
       else:
           for move in range(len(listOfMoves)):
               currentMove = listOfMoves[move]
               (rowC, colC) = transform_coords(currentMove[0], currentMove[1])
               newBoard = copy.deepcopy(board)
               newBoard.set_piece(rowC, colC, color)
               # print('newBoard Position: row', rowC, 'col', colC, 'Board:')
               # print(newBoard)
               result = min_max_algo(newBoard, Ocolor, depth + 1, goalDepth, False, color, alpha, beta)
               if (maxValue <= result) and depth == 0:
                   # print(bestMove)
                   bestMove = [rowC, colC]

               maxValue = max(maxValue, result)
               alpha = max(alpha, result)
               if beta <= alpha:
                    break
           return maxValue
   else:
       minValue = 999999
       listOfMoves = get_valid_moves(board, color)
       if depth == goalDepth:
           return eval_func(board, color)
       else:
           for move in range(len(listOfMoves)):
               currentMove = listOfMoves[move]
               (rowC, colC) = transform_coords(currentMove[0], currentMove[1])
               newBoard = copy.deepcopy(board)
               newBoard.set_piece(rowC, colC, color)
               result = min_max_algo(newBoard, Ocolor, depth + 1, goalDepth, True, color, alpha, beta)
               if (minValue >= result) and depth == 0:
                   # print(bestMove)
                   bestMove = [rowC, colC]
               minValue = min(minValue, result)
               beta = min(beta, result)
               if beta <= alpha:
                   break
       return minValue


def get_valid_moves(board: Board, color: PieceColor) -> list:
   """
   Check if there exists a valid move for the given color
   :param color: PieceColor
   :return: list of valid moves, empty list if not
   """
   moves = []
   for row in range(8):
       for col in range(8):
           piece = Board._get_piece(board, row, col)
           # print(board.board[row * 8 + col])
           # print(row, col)
           # print(len(board.board))
           #print(board.board[row * 8 + col])
           #print(row, col)
           #print(len(board.board))
           if (piece == PieceColor.NONE) and len(Board._get_enveloped_pieces(board, row, col, color)) > 0:

               moves.append([row,col])
   return moves

def eval_func(board: Board, colorE: PieceColor) -> float:
    evalF = 0
    numF = 0
    orangep = 0
    bluep = 0
    """
    Get opponent of given player
    :param player: Board currently being played
    :return: evaluation for current position
    """
    for rowE in range(8):
        for col in range(8):
            piece = Board._get_piece(board, rowE, col)
            '''factor 1: number of pieces for each color are a consideration to winning an othello game'''
            if piece == PieceColor.ORANGE:
                evalF += .02
                orangep += 1
            if piece == PieceColor.BLUE:
                evalF -= .02
                bluep += 1

            '''factor 2: corner pieces are crucial to winning an  othello game'''
            if (piece == PieceColor.ORANGE) and (((rowE == 1) and (col == 1)) or
                                                 ((rowE == 8) and (col == 1)) or
                                                 ((rowE == 1) and (col == 8)) or
                                                 ((rowE == 8) and (col == 8))):
                evalF += 5
            if (piece == PieceColor.BLUE) and (((rowE == 1) and (col == 1)) or
                                               ((rowE == 8) and (col == 1)) or
                                               ((rowE == 1) and (col == 8)) or
                                               ((rowE == 8) and (col == 8))):
                evalF -= 5
            if (piece == PieceColor.NONE):
                numF += 1
    numOfPieces = 64 - numF
    '''factor 3: number of available moves are important to winning an othello game'''
    if colorE == PieceColor.ORANGE:
        evalF += get_valid_moves(board, colorE).__sizeof__() / (numOfPieces * 100)
    if colorE == PieceColor.BLUE:
        evalF -= get_valid_moves(board, colorE).__sizeof__() / (numOfPieces * 100)
    if ourPlayer==PieceColor.BLUE:
        evalF=-evalF
    #This is our utility function
    if numOfPieces == 64 or (len(get_valid_moves(board, PieceColor.BLUE)) == 0 and len(
            get_valid_moves(board, PieceColor.BLUE)) == 0):
        if bluep > orangep:
            if ourPlayer== PieceColor.ORANGE:
                evalF = -100000
            else:
                evalF = 100000
        if bluep < orangep:
            if ourPlayer== PieceColor.ORANGE:
                evalF = 100000
            else:
                evalF = -100000
        if bluep == orangep:
            evalF = 0
    return evalF

#board = [PieceColor.NONE] * 64

game = Game("p1", "p2")
# print("Initial Board:\n{b}\n".format(b=game.board))
# def __init__(self):
#     """
#     Initialize Othello board
#     """
#     # Setup initial board state
#     self.set_piece(5, 'D', PieceColor.BLUE)
#     self.set_piece(5, 'E', PieceColor.ORANGE)
#     self.set_piece(4, 'D', PieceColor.ORANGE)
#     self.set_piece(4, 'E', PieceColor.BLUE)
#
# game = Game("str1", "str2")
#
#
# if not game.board.is_full():
#     print("I am not full")
first = True #flag used to get the color of the player
#while the game is being played
color = PieceColor.NONE
OColor = PieceColor.NONE
while True:
   if os.path.isfile("./referee/end_game"):
        with open("./referee/end_game", "r") as fp:
            end = fp.readlines()
            print("end:", end)
        fp.close()
        with open("./referee/move_file", "r") as fp:
            # Get last non-empty line from file
            line = ""
            for next_line in fp.readlines():
                if next_line.isspace():
                    break
                else:
                    line = next_line

                # Tokenize move
            if not line == "":
                tokens = line.split()
                group_name = tokens[0]
                col = tokens[1]
                row = tokens[2]
                (rowC, colC) = interpret_coords(int(tokens[2]), tokens[1])
                # making sure it is a valid move and giving a reason why if it is not a valid move
                # If column is P, get valid moves of Ocolor, if list greater than 0
                if tokens[1] == 'P':
                    valid_moves = get_valid_moves(game.board, OColor)
                    if len(valid_moves) > 0:
                        print("Move: {m}".format(m=line.rstrip()), " is an invalid move, tried to pass when valid move was possible")
                # get enveloped pieces, if 0 then invalid move

                elif Board._get_piece(game.board, rowC, colC) == PieceColor.BLUE or Board._get_piece(game.board, rowC, colC) == PieceColor.ORANGE:
                    print("Move: {m}".format(m=line.rstrip()), " is an invalid move, cell already occupied")
                elif out_of_bounds(rowC, colC) == True:
                    print("Move: {m}".format(m=line.rstrip()), " is an invalid move, out of bounds")
                # I thinkg set piece already checks if it is a valid move, returns false if not valid move
                # but we need to give reasons why
                elif len(Board._get_enveloped_pieces(game.board, rowC, colC, OColor)) == 0:
                    print("Move: {m}".format(m=line.rstrip()), " is an invalid move, does not envelop any pieces")
                # get piece, if color is blue or orange, invalid move

        sys.exit(1)
   while os.path.isfile("./referee/agony.go"): #get the file the referee made
       if first:
           #if nothing in the move file, the player's color is blue
           if os.stat("./referee/move_file").st_size==0:
               print("I am first player")
               color = PieceColor.BLUE
               OColor = PieceColor.ORANGE
               ourPlayer = PieceColor.BLUE
               first = False #set flag to false so do not check the color again
           #if there is already a line in the move file and the flag is still true, the player's color is orange
           else:
               print("I am second player")
               color = PieceColor.ORANGE
               OColor = PieceColor.BLUE
               ourPlayer = PieceColor.ORANGE
               first = False


       #we first need to update the board by reading move file
       #mtime = os.path.getmtime("./referee/move_file")
       #modified = False

       #if os.path.getmtime("./referee/move_file") > mtime:
           #modified = True
           #break

       #if modified:
       with open("./referee/move_file", "r") as fp:
               # Get last non-empty line from file
           line = ""
           for next_line in fp.readlines():
               if next_line.isspace():
                   break
               else:
                   line = next_line

               # Tokenize move
           if not line=="":
               tokens = line.split()
               group_name = tokens[0]
               col = tokens[1]
               row = tokens[2]
               (rowC, colC) = interpret_coords(int(tokens[2]), tokens[1])
               game.board._set_piece(rowC, colC, OColor)  # updates board


       fp.close()

       #first check if board is full -- do we need to do this??
       #then check if there are any possible moves

       #get possible moves and put those coordinates in list
       newBoard = copy.deepcopy(game.board)
       t = time.time()
       num =0

       while (time.time() - t < 2):
            # print(time.time() - t)
            # print(num)
            currentMove = copy.deepcopy(bestMove)
            min_max_algo(newBoard, color, 0, num, True, OColor, -1000000, 1000000)
            num+=1
       # min_max_algo(game.board, color, 0, 5, True, OColor, -100000, 100000)
       # print("Initial Board:\n{b}\n".format(b=game.board))

       f = open("./referee/move_file", 'a')  # open the move file to make a move
       # write the desired move in the move file
       #print("GroupX ", str(topMove[1]), " ", str(row))
       #f.write("GroupX E 3")


       if Board.has_valid_move(game.board, color):

           stringToWrite = ('agony ' + str(currentMove[1]) + " " + str(currentMove[0]) + "\n")
           f.write(stringToWrite)  # write the desired move in the move file
           f.close()  # close the file until need to wirte to it again
           # print("String to write ", stringToWrite)
           # print(game.board)
           game.board.set_piece(currentMove[0], currentMove[1], color)  # update our board
           bestMove = None
           time.sleep(0.5);

       else:

           stringToWrite = ('agony ' + "P " + "3\n")
           f.write(stringToWrite)  # write the desired move in the move file
           f.close()  # close the file until need to wirte to it again
           time.sleep(0.5);


