import os.path
import sys
from Board import PieceColor, Board, transform_coords
from referee.Game import Game
import time


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
    print(moves)
    return moves


'''input: the board, the player color that is going next
result: positive float means better for orange, negative float means better for blue'''


def eval_func(board: Board, colorE: PieceColor) -> float:
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
            if piece == PieceColor.ORANGE:
                evalF += .02
            if piece == PieceColor.BLUE:
                evalF -= .02
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
            if piece == PieceColor.NONE:
                numF += 1

    numOfPieces = 64 - numF


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
    while os.path.isfile("./referee/Player1.go"): #get the file the referee made
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

                game.board.set_piece(int(row), str(col), OColor) #updates board


        fp.close()

        #first check if board is full -- do we need to do this??
        #then check if there are any possible moves

        #get possible moves and put those coordinates in list
        moves = get_valid_moves(game.board, color)
        # get the number of pieces it would change for each possible move and store in array
        rankedMoves = []
        for index in range(len(moves)):
            changedMoves = Board._get_enveloped_pieces(game.board, moves[index][0], moves[index][1], color)
            numChanged = len(changedMoves)

            rankedMoves.append([moves[index][0], moves[index][1], numChanged])
        rankedMoves.sort(key=lambda tup: tup[2], reverse=True)
        print("Ranked Moves:", rankedMoves)
        # sort this list and use the move with the most possible moves

        topMove = rankedMoves[0]
        row = topMove[0]
        (rowC, colC) = transform_coords(row, topMove[1])
        f = open("./referee/move_file", 'a')  # open the move file to make a move
        # write the desired move in the move file
        #print("GroupX ", str(topMove[1]), " ", str(row))
        #f.write("GroupX E 3")
        stringToWrite = ('Player1 ' + str(colC) + " " + str(rowC)+ "\n")
        f.write(stringToWrite)  # write the desired move in the move file
        f.close()  # close the file until need to wirte to it again
        game.board.set_piece(rowC, colC, color) #update our board
        time.sleep(1);

