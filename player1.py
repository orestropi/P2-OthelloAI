import os.path

first = True #flag used to get the color of the player

#while the game is being played
while True:
    while os.path.isfile("./referee/player1.py.go"): #get the file the referee made
        if first:
            #if nothing in the move file, the player's color is blue
            if os.stat("./referee/move_file").st_size==0:
                print("I am first player")
                color = "blue"
                first = False #set flag to false so do not check the color again
            #if there is already a line in the move file and the flag is still true, the player's color is orange
            else:
                print("I am second player")
                color = "orange"
                first = False
        f = open("./referee/move_file", 'w') #open the move file to make a move
        f.write("GroupX D 3") #write the desired move in the move file
        f.close() #close the file until need to wirte to it again