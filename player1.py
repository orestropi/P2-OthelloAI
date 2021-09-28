import os.path
import sys
from Board import PieceColor, Board
from referee.Game import Game


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
            if (piece == PieceColor.NONE):
                numF += 1

    numOfPieces = 64 - numF

    '''factor 3: number of available moves are important to winning an othello game'''
    if colorE == PieceColor.ORANGE:
        evalF += get_valid_moves(board, colorE).__sizeof__() / numOfPieces
    if colorE == PieceColor.BLUE:
        evalF -= get_valid_moves(board, colorE).__sizeof__() / numOfPieces

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
    while os.path.isfile("./referee/player1.py.go"): #get the file the referee made
        if first:
            #if nothing in the move file, the player's color is blue
            if os.stat("./referee/move_file").st_size==0:
                print("I am first player")
                color = "blue"
                color = PieceColor.BLUE
                first = False #set flag to false so do not check the color again
            #if there is already a line in the move file and the flag is still true, the player's color is orange
            else:
                print("I am second player")
                color = "orange"
                color = PieceColor.ORANGE
                first = False



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
        if topMove[1] == 0:
            letter = "A"
        elif topMove[1] == 1:
            letter = "B"
        elif topMove[1] == 2:
            letter = "C"
        elif topMove[1] == 3:
            letter = "D"
        elif topMove[1] == 4:
            letter = "E"
        elif topMove[1] == 5:
            letter = "F"
        elif topMove[1] == 6:
            letter = "G"
        elif topMove[1] == 7:
            letter = "H"
        f = open("./referee/move_file", 'w')  # open the move file to make a move
        # write the desired move in the move file
        f.write("GroupX", str(topMove[1]), str(row))  # write the desired move in the move file
        f.close()  # close the file until need to wirte to it again
