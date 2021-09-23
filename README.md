Project 2: Game Playing
CS4341
Project 2 - A Term 2021
Prof. Carolina Ruiz
Due Dates:
Initial Project Submission: by Friday, Oct. 1st, 2021 at 9:00 pm. (See late submission policy for this project at the end of this page.)
Tournament Submission: by Monday, Oct. 11th, 2021 at 10:00 AM morning (no late submissions will be accepted, no exceptions.)
Teams:
Students are expected to organize themselves in groups of exactly 3 students for this project. 
 The Team Formation discussion board can be used to find other students looking for a group.
Once that you have formed your team, please create a Group on our Canvas course site by going to "People" (on the leftmost menu bar) and from there to "Project 2 Groups".
Name the Group with the name you'll use for your player (see instructions below) and add all members of your team to the Group.
Programming language:
Your team can implement your program in any programming language of your choice.
Referee (provided):
the referee is available here  Download here.
Questions? If you have any questions about the project:
re-read the project description below
read postings and replies on the project 2 discussion board (someone may have asked the same question before)
if you still have a question, please post it on the project 2 discussion board.
come to office hours

PROJECT DESCRIPTION AND GOAL
This project consists of developing and implementing a computer program that plays Othello. To some this game is also known as Reversi. The project will exemplify the minimax algorithm and alpha-beta pruning.


GAME DESCRIPTION
(For simplicity, the following game description will use "it" to refer to a player, as the player will be a computer program you'll write.)

Othello is a two player game (one of them being your computer program). The two players take turns putting "discs" (or pieces, stones or marks) on a board. The classical game board is an 8 by 8 grid. At the start of the game there are four discs in the center of the grid. Blue in the top-right and bottom-left. Orange in the top-left and bottom-right. (See Figure 1 for initial configuration.) Players take turns placing discs on the board until the board is full or no legal moves remain. The object is to catch opponent's discs between two of your discs to flip them to your color. At the end of the game, whoever has the most discs on the board wins. 

Please look for information online about Othello and its rules. A good website to play the game and learn about the Othello rules is:  https://www.eothello.com/ (Links to an external site.). See 'How to play Othello" on that page. Their website states: "We recommend Brian Rose's book "Othello: a minute to learn... a lifetime to master" (Links to an external site.). Brian is the 2001 World Othello Champion and his is the most comprehensive book on Othello strategy ever published in English. "

Discs
One of the players uses blue discs and the other one uses orange discs.
blue / orange were chosen for this project because they form a colorblind-friendly palette.
Board
We will use an 8x8 board.
We will label the board as in Figures 1-3: columns A through H (left to right), and the rows 1 through 8 (bottom to top).
 

othello-boards.png

 

Moves
The player with the blue discs moves first.
There are two types of legal moves:
Moves that trap at least one opponent disc between pre-existing discs of your color on the board and the currently placed disc. This trapping could be horizontal, vertical, or diagonal. All of your opponent discs that are trapped between any of your pre-existing discs and your newly placed disc in any direction (horizontally, vertically and/or diagonally) are flipped to your color.
The other legal move is a PASS. This move can only be taken when there are no trapping legal moves available for the player to take. 
Moves will alternate between blue and orange. We will describe a move as a pair: (column row) where:
column is a letter from A to H, or P for passing
row is a number from 1 to 8, (doesn't matter which number if column=P, but do include a number)
IMPORTANT: If a player chooses an illegal move, then the player will automatically lose the game. The following are illegal moves:
placing a disc in a cell that is already occupied,
placing a disc in a cell outside the board,
placing a disc in a cell that doesn't trap opponent's discs (e.g., the cell is not adjacent vertically, horizontally or diagonally to a sequence of one or more opponent's discs that ends at one of the player's discs),
using a PASS when there are other legal moves available to the player.
For example, a possible first move of the game is (E 3), meaning that a blue disc is placed in column E (the fifth from the left), and it occupies row 3 (the third from the bottom). This would result in the orange disc at (E,4) being converted to a blue disc (see Figure 2). It would then be player 2's turn. A possible move for Orange would be (F 3), placing an orange disc in column F, row 3. This results in the blue disc at (E,4) being converted to an orange disc (see Figure 3). 
Game Rules
        A game will consist of a sequence of the following actions:

A random selection method is used to determine which player will use the blue discs and which player will use the orange discs. In what follows, the player who gets to use the blue discs is called player1 and the player who gets to use the orange discs is called player2.
Player 1 (the one with blue discs) gets to play first.
After that, the players take turns moving.  A move (column row) must satisfy the following constraints:
Time Limit: There is a time limit time-limit for a player to make its move. This time limit is in user time, not CPU time. Please use a variable called time-limit in your code. For now, we'll use time-limit = 10 seconds. Once that you start testing your players and we have a good idea of what value would be reasonable, we can all make a joint decision about the value for this time limit.
Move pre-conditions (if not passing):
(column, row) is a valid board location (A <= column <= H, 1 <= row <= 8).
There is no disc at (column, row).
There is a sequence of one or more opponent discs adjacent to (column, row) in at least one of eight directions (up, up-right, right, right-down, down, down-left, left, left-up) that is/are trapped between a disc of the player's color and (column, row).
Move post-conditions (if not passing)
After the move, the cell at column and row on the board will be occupied by a disc of the player's color.
For each of eight directions (up, up-right, right, right-down, down, down-left, left, left-up) any sequence of opponent discs trapped between to (column, row) and a pre-existing disc of the player's color is converted to a player's color disc.
It will be the other player's turn next.
Move pre-conditions (if passing, that is column = P)
There is no unoccupied (column, row) cell on the board with the necessary sequence of opponent discs trapped between this cell and player's pre-existing discs.
Move post-conditions (if passing, that is column = P)
The board configuration remains unchanged
It will be the other player's turn next.
The game ends in any of the following cases:
The board is full. The player with the most discs wins the game, and the other loses the game. If the number of discs is equal, then the game is a draw.
Neither player can make a legal move. The player with the most discs wins.
A player makes an illegal move - the other player wins.
A player fails to move within the time limit - the other player wins. 
PROJECT ASSIGNMENT
The project assignment consists of the following:

Your group must implement a program that plays Othello.
Each group needs to pick a one-word name for their program.
Your program must use the minimax algorithm with alpha-beta pruning.
Use a utility function (also called static evaluation) of your choice.
If your minimax with alpha-beta pruning cannot expand the whole search tree in the time allowed, your program must use a game strategy:
Use an evaluation function of your choice to be able to evaluate non-terminal board configurations and thus avoid expanding the whole minimax tree. Remember that your evaluation function must coincide with (i.e., be equal to) your utility function on terminal board configurations.
Also, implement heuristics to decide which nodes in the game tree to continue expanding and which nodes not to expand any further.
For sample evaluation functions and heuristic game strategies study Sections 5.1-5.3 of Russell and Norvig's textbook and the adversarial search lecture slides; and investigate approaches described in other books or online sources. We recommend using the progressive deepening heuristic. 
The better your evaluation function and your heuristic game strategy, the better your program will play, and the better your grade in the project.
Your program must produce only valid moves.
Your program must be able to read each of the opponent's moves, verify that they are valid, and execute them. (The process is described in the following section.) If the opponent's move is invalid, your program must display the offending move, and state the error (e.g., space occupied, no trap).
 Your program must detect if the game has come to an end, and if so, it must print a message stating who won.  
Your program must follow the specification given in this project so that it can interface with other groups' programs.
If you want, you may implement a graphical interface for your program, that displays the configuration of the board during the game. Such an interface is NOT required. (As described below, a referee program will be provided which will display the board during a game.)
Your player must not consume computing resources during your opponent's turn. In this spirit, when it is your opponent's turn, your player should simply check for the signal from the referee that it is your turn to move.
Note that finding a good utility function, a good evaluation function and good heuristics depends heavily on the experience you have with the game. We recommend that you start playing the game and getting the flavor of what a good Othello strategy is. Also, research the strategies that other people have used for this and other games. Lots of information can be found in the references listed in your syllabus, the web, and magazine articles. 

Please note: Although you are welcome to look at code and systems available online to guide the design of your program, you MUST submit your own original code.

PROGRAM COMMUNICATION
There are many communication methods that are far more elegant and efficient than this one, but the intent is that this method will result in the least elaborate code, and that it allows you to implement your program in your choice of programming languages. The debugging process is also simple since you can control the contents of these files with the use of any text editor. All the moves are communicated through a file accessible to both players.

Each group needs to pick a one-word name for their program. We'll refer to that name as groupname in what follows. You must use this same name on the Group you will create in Canvas for your Project 2.
Each group must submit the code of their program and an executable (or script) named groupname.
A referee program, described below, will be told what two groups are going to play. The referee will decide at random which player goes first, check the validity of the moves, check for game ending conditions, and maintain the communication between the two groups' programs. The referee program is provided on this project description. You do NOT have to write the referee program.
In most parts of this document, we will refer to the referee program as "the referee" or simply "Referee".
The referee will maintain four text files: a file called move_file , two groupname.go files (one for each group) and an end_game file that will be created upon the completion of the game and which will contain the final outcome of the game (e.g., the winning player, if any). Note: not all four of these files will exist at all times as they are used to control the flow of turns. Please see below for more details.
The presence of a groupname.go file indicates that it is that player's turn. When groupname.go file appears in the directory, the groupname's program should first check to see if an end_game file exists. If this file exists, it means that the game is over and this file contains the result of the game as described below. If the end_game file doesn't exist then the groupname's program should read the opponent's move from move_file, pick its own move, and overwrite move_file with its own move. When groupname.go is absent in the directory, the groupname's program should simply wait for it to appear.
A move will have the following format: <groupname> <column> <row> (e.g., "myGroup E 3" but without the " " around the move)
At the beginning of the game, each player should wait until the file groupname.go with its groupname appears in the directory. The player then reads move_file . If this file is empty, then this means that the groupname player will play with blue discs and hence makes the first move. Otherwise, if a move already exists in move_file , then the groupname player will play with orange discs and needs to make the next move.
Each player is allowed a maximum of time-limit seconds to make its move. The timer starts as soon as the groupname.go file appears, and a move is considered done 100 ms after a write to move_file is made. (This is because the referee polls move_file every 50 ms to see if its timestamp has changed. After it detects a change it then waits 100 ms to allow the team to finish writing out their move and then reads the move from the file. This allows the player's program time to write out in case the polling happened right as they opened the file. The player program's file write should NOT take any longer than 100 ms. Your player needs to open the file for writing, write the move and close the file all in one concise operation to ensure the referee reads in what the player means.
The two groups' players now take turns making moves until the end_game file is created. The possible messages the referee can write on the end_game file are:
END: <winning_groupname> WINS! <losing_groupname> LOSES! <reason>
where reason can be any of the following:
The winning player has more discs on the board!
Time out!
Out-of-order move!
Invalid move!
END: Match TIED!
To summarize, each group's program does the following:
Wait until groupname.go appears in the directory.
Read in the move from move_file and calculate its own next move using minimax with alpha-beta pruning.
Write its move to move_file (overwriting the content of that file).
Repeat until the end_game file is created by the referee announcing that the game is over!

For illustration purposes, here is an example sequence of events that happens in a game between two groups GroupX and GroupY.

GroupX and GroupY programs start and wait for their respective "go" files.
Referee starts and creates the file move_file. Referee then randomly selects a group as the first player. Let's assume that player is GroupX.
Referee creates the file GroupX.go and starts timing.
GroupX detects the presence of the GroupX.go file, reads move_file, finds out it is empty, and knows it is the first player and will play with blue discs.
GroupX calculates its move (let's say E 3) and writes in move_file the line "GroupX E 3" (without the " ") within time-limit seconds.
The current content of move_file is
     GroupX E 3  
Referee detects a change in move_file, waits 100 ms, reads the move, checks timing and validity of move, checks if the game has ended.
Since the game hasn't ended yet, Referee deletes the GroupX.go file and creates GroupY.go.
GroupY detects the presence of the GroupY.go file, reads move_file, finds out it is NOT empty, and knows it is the second player and will play with orange discs.
GroupY reads GroupX's move, calculates its own move (let's say F 3) and writes in move_file the line "GroupY F 3" (without the " ") within time-limit seconds.
The current content of move_file is
     GroupY F 3 
The process above is repeated until there is an invalid / late / out-of-order move, or if one of the players wins, or if there are no valid moves for any of the players. In each of these cases, the referee program creates the end_game file and writes a corresponding message to it as described above. The referee also creates both groupname.go files so that both players are prompted to look for the end_game file. Let's suppose GroupY wins. Then the end_game file will contain:
     END: GroupY WINS! GroupX LOSES! The winning player has more discs on the board! 
All programs stop running.
REFEREE
A referee program to conduct the game is provided here  Download here(you don't have to write it). The functions of the referee have been detailed in the previous section.

Specifically, the referee program will be in charge of:

Assigning which program goes first, as described above.
Displaying a graphical depiction of the board configuration after each move.
Giving turns to each of the playing programs. By creating the file groupname.go, the referee program is giving the turn to groupname.
Timing each of the players. It starts measuring the time for groupname's move just after creating groupname.go.  If a program exceeds its time limit, the referee program will stop the game, announcing that the offending program has lost. (Note that your program should not time its opponent.)
Detecting invalid moves. If the referee program finds an invalid move, it will stop the game, announcing that the offending program has lost.
Ending the game when all positions on the board are occupied or no more valid moves exist, announcing either a winner and a loser, or a tie.
If you find any issues or bugs with this referee program, or any deviations from the specifications provided on this webpage, PLEASE report them on the Canvas Project 2 discussion board immediately. In such event, we will try to fix any bugs, update the version of the referee program and notify the class.

REPORT SUBMISSION AND DUE DATE
Initial Project Submission: Deadline: Friday, Oct. 1st at 9:00 pm

By this deadline, one (and only one) member of your group must submit the following files using Canvas:

Documentation
The names of the members of your group. A detailed description of what each teammate contributed to the project.
Instructions on compiling and running your program.
The utility function that your program uses.
The evaluation function that your program uses.
The heuristics and/or strategies that you employed to decide how to expand nodes of the minimax tree without exceeding your time limit.
Results:
describe which tests you ran to try out your program. Did your program play against human players? Did your program play against itself? Did your program play against other programs? How did your program do during those games?
describe the strengths and the weaknesses of your program.
A discussion of why the evaluation function and the heuristic(s) you picked are good choices.
Code.  
The source code for your program
Ancillary files, if any, that your program requires (e.g., such as a script to run a language interpreter).
Please note: Although you are welcome to look at code and systems available online to guide the design of your program, you MUST submit your own original code.

Tournament Submission: Deadline: Monday, Oct. 11th at 10:00 am

By this deadline, one (and only one) member of your group must submit the following files using Canvas:

Documentation
A detailed yet concise description of what your group changed in your player since the initial project submission. A detailed description of what each teammate contributed to the new submission since the initial submission.
Code.  
The source code for your program
Ancillary files, if any, that your program requires (e.g., such as a script to run a language interpreter).
Please note: Although you are welcome to look at code and systems available online to guide the design of your program, you MUST submit your own original code. Also, we will compare your initial code and your tournament code to identify work that you did in between submissions.

TOURNAMENT
A tournament will be held where the students' programs will compete against one another!
Each group will be allowed to keep working on and improve their programs submitted for Project 2 on Oct. 1st. Before the tournament, all groups will submit the updated tournament version of their code via Canvas. The deadline for making the tournament submissions is Monday, Oct. 11th by 10:00 AM (morning).
Note however that the majority of your project grade will come from your initial project 2 submission. See Grading Criteria below.

The final rounds of the tournament will be held during class on Tuesday Oct 12 2021.
Groups whose program perform well in the tournament will receive bonus points.
 

Tournament Rules:
You must submit via Canvas by the re-submission deadline either a new, improved player or a note asking us to use your original player in the tournament.
Your player must not consume computing resources during your opponent's turn. In this spirit, when it is your opponent's turn, your player should simply check for the signal from the referee that it is your turn to move.
Both players will be executed on the same machine, and must not spawn processes on any other machine.
The new player you submit on Oct. 11th will play against your original player from Oct. 1st.
If your new player wins, then your group will earn 5 points (see full list of extra points below in the Grading Criteria).
The winner of this match will represent your team in the tournament.
 

Tournament Structure:
The tournament structure will mimic that of soccer's World Cup, but the precise structure will be determined when we know how many players will participate. However, every participating player is guaranteed at least 2 games.
First Round: Each player will be randomly assigned to one of 4 groups of about 4 or 5 players. Each player will play against every other player in its group.
Second Round: The best 2 players in each group from the first round will move on to this round. Each of these 8 players will be assigned to one of 2 groups of 4. Each player will play against every other player in its group.
Semi-Final Round: The best 2 players in each group from the second round will move to this round. Each of these 4 players will play against every other player in this group.
Final Round: The bottom 2 players from the semi-final round will play each other for the third place, and the top 2 players from the semi-final round will play each other for the first place.
"In the end, there can be only one." :-)
CS4341-TournamentStructure.jpg
Tournament Date and Time:
First, Second, and Semi-Final Rounds will be held on Monday afternoon, October 11th promptly after we receive your submissions. Results from these rounds will be announced in class on Tuesday, Oct. 12th (but not before then).
Unless one of the finalist teams object, the Final Round games will be played live in class on Tuesday, Oct. 12th.
GRADING CRITERIA:

Initial Project 2 Submission on Oct. 1st:
35 points:	minimax implementation
15 points:	alpha-beta pruning
15 points:	heuristic evaluation function; that is, function that assigns a number to any intermediate board configuration.
15 points:	heuristic strategy to avoid expanding the whole minimax tree so that a move is produced within the time limit.
10 points:	playing "reasonably well"; that is, showing evidence of good offensive and defensive behavior.
10 points:	interacting well with referee and good documentation
----------	 
100 points	 
Tournament Submission on Oct. 11th:
You will receive extra credit on project 2:
Extra points:	Optional: using machine learning (e.g., decision trees, neural networks, ...) to make your system better at playing the game. If you do so, please point that out in a readme file with your re-submission explaining what you did
5 points:	if your new player (from Oct. 11th) wins again your original player (from Oct. 1st)
5 points:	for successfully completing at least one game (with a win, loss, or draw) during the tournament
+2 point:	for EACH game that your player wins in the tournament
+1 point:	for EACH game that your player draws in the tournament
Note that the winning player may earn as many as 30 extra points: 5 points if the resubmission wins over the original submission; 5 for successfully completing a game; 6 points per round if it wins each game it plays on the 1st, 2nd and semi-final rounds; and 2 points in the final round.


LATE SUBMISSION POLICY:


Initial Project 2 submission deadline is Tuesday Oct. 1st at 9 pm.

Late submissions will be accepted with a 5*H points penalty, where H is the numbers of hours (or fraction of an hour) you submit your project after the deadline:
For example, if you submit your project after the deadline but between 9:01 pm and 10:00 pm, then you'll get a 5 point penalty; if you submit between 10:01 pm and 11:00 pm you'll get a 10 point penalty; if you submit between 11:01 pm and 12:00 midnight, you get a 15 point penalty and so on (adding 5 points per hour).
Hence, no submissions will be accepted after Sat Oct 2nd at 5 pm since at that point the penalty will reach 100 points.
Once that your project submission is graded, 5*H points will be taking off from your score. For example, if you submit your project within 4 hours after the deadline and your project score is say 92 points, then your project 2's initial submission grade will be 92 - (4*5) = 72.
 
Tournament Project 2 submission deadline is Monday Oct. 11th at 10 AM/morning.
No late Tournament submissions will be accepted. No exceptions.

test
