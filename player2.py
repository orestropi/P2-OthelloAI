import os.path
import sys
from Board import PieceColor, Board, transform_coords
from referee.Game import Game
import time
import copy

depth = 0
maxPlayer = True
goalDepth = 1
bestMove = []


def min_max_algo(board: Board, color: PieceColor, depth, maxPlayer: bool, Ocolor: PieceColor, alpha: int, beta: int) -> float:
    global bestMove
    if maxPlayer:
        maxValue = -99999
        listOfMoves = get_valid_moves(board, color)
        if depth == goalDepth:
            return eval_func(board, color, OColor)
        else:
            for move in range(len(listOfMoves)):
                result = eval_func(board, color, OColor)
                currentMove = listOfMoves[move]
                (rowC, colC) = transform_coords(currentMove[0], currentMove[1])
                board.set_piece(rowC, colC, color)
                newBoard =  copy.deepcopy(board)
                board.set_piece(rowC, colC, PieceColor.NONE)
                print('newBoard Position: row', rowC, 'col', colC, 'Board:')
                print(newBoard)
                min_max_algo(newBoard, Ocolor, depth + 1, False, color, alpha, beta)
                if (maxValue < result) and depth == 0:
                    print(bestMove)
                    bestMove = [rowC, colC]
                alpha = max(alpha, result)
                if beta <= alpha:
                    break
                maxValue = max(maxValue, result)
            return maxValue
    else:
        minValue = 99999
        listOfMoves = get_valid_moves(board, color)
        if depth == goalDepth:
            return eval_func(board, color, OColor)
        else:
            for move in range(len(listOfMoves)):
                result = eval_func(board, color, OColor)
                currentMove = listOfMoves[move]
                (rowC, colC) = transform_coords(currentMove[0], currentMove[1])
                board.set_piece(rowC, colC, color)
                newBoard =  copy.deepcopy(board)
                board.set_piece(rowC, colC, PieceColor.NONE)
                min_max_algo(newBoard, Ocolor, depth + 1, True, color, alpha, beta)
                if (minValue > result) and depth == 0:
                    print(bestMove)
                    bestMove = [rowC, colC]
                beta = min(beta, result)
                if beta <= alpha:
                    break
                minValue = min(minValue, result)
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

def eval_func(board: Board, colorE: PieceColor, colorO: PieceColor) -> float:
    evalF = 0
    numF = 0
    """
    Get opponent of given player
    :param player: Board currently being played
    :return: evaluation for current position
    """
    for rowE in range(8):
        for col in range(8):
            piece = Board._get_piece(board, rowE, col)
            '''factor 1: number of pieces for each color are a consideration to winning an othello game'''
            if piece == colorE:
                evalF += .02
            if piece == colorO:
                evalF -= .02
            '''factor 2: corner pieces are crucial to winning an  othello game'''
    #         if (piece == PieceColor.ORANGE) and (((rowE == 1) and (col == 1)) or
    #                                              ((rowE == 8) and (col == 1)) or
    #                                              ((rowE == 1) and (col == 8)) or
    #                                              ((rowE == 8) and (col == 8))):
    #             evalF += 5
    #         if (piece == PieceColor.BLUE) and (((rowE == 1) and (col == 1)) or
    #                                            ((rowE == 8) and (col == 1)) or
    #                                            ((rowE == 1) and (col == 8)) or
    #                                            ((rowE == 8) and (col == 8))):
    #             evalF -= 5
    #         if (piece == PieceColor.NONE):
    #             numF += 1
    #
    # numOfPieces = 64 - numF
    #
    # '''factor 3: number of available moves are important to winning an othello game'''
    # if colorE == PieceColor.ORANGE:
    #     evalF += get_valid_moves(board, colorE).__sizeof__() / numOfPieces
    # if colorE == PieceColor.BLUE:
    #     evalF -= get_valid_moves(board, colorE).__sizeof__() / numOfPieces

    return evalF


#board = [PieceColor.NONE] * 64

game = Game("p1", "p2")
print("Initial Board:\n{b}\n".format(b=game.board))
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
while True:
   while os.path.isfile("./referee/player2.go"): #get the file the referee made
       if first:
           #if nothing in the move file, the player's color is blue
           if os.stat("./referee/move_file").st_size==0:
               print("I am first player")
               color = PieceColor.BLUE
               OColor = PieceColor.ORANGE
               first = False #set flag to false so do not check the color again
           #if there is already a line in the move file and the flag is still true, the player's color is orange
           else:
               print("I am second player")
               color = PieceColor.ORANGE
               OColor = PieceColor.BLUE
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
               if tokens[1] != "P":
                game.board.set_piece(int(row), str(col), OColor) #updates board


       fp.close()

       #first check if board is full -- do we need to do this??
       #then check if there are any possible moves

       #get possible moves and put those coordinates in list
       newBoard = copy.deepcopy(game.board)
       min_max_algo(newBoard, color, 0, True, OColor, -1000000, 1000000)
       print("Initial Board:\n{b}\n".format(b=game.board))

       f = open("./referee/move_file", 'a')  # open the move file to make a move
       # write the desired move in the move file
       #print("GroupX ", str(topMove[1]), " ", str(row))
       #f.write("GroupX E 3")
       if Board.has_valid_move(game.board, color):
           stringToWrite = ('Player2 ' + str(bestMove[1]) + " " + str(bestMove[0]) + "\n")
           f.write(stringToWrite)  # write the desired move in the move file
           f.close()  # close the file until need to wirte to it again
           game.board.set_piece(bestMove[0], bestMove[1], color)  # update our board
           time.sleep(1);

       else:
           stringToWrite = ('Player2 ' + "P " + "3\n")
           f.write(stringToWrite)  # write the desired move in the move file
           f.close()  # close the file until need to wirte to it again
           time.sleep(1);


