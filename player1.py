import os.path

first = True
while True:
    while os.path.isfile("./referee/player1.py.go"):
        if first:
            if os.stat("./referee/move_file").st_size==0:
                print("I am first player")
                color = "blue"
                first = False
            else:
                print("I am second player")
                color = "orange"
                first = False