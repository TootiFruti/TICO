import random

def boardDraw(moves):
    print(f"""
     |      |  
  {moves[0]}  |   {moves[1]}  |  {moves[2]}
____ | ____ | ____ 
     |      |
  {moves[3]}  |   {moves[4]}  |  {moves[5]}
____ | ____ | ____ 
     |      |
  {moves[6]}  |   {moves[7]}  |  {moves[8]}
     |      |


    """) 
    
def computerMove(moves, mark, isGameLoaded):
    if isGameLoaded[0]==1:
        isGameLoaded[0]=0 
        choice=None
    else:
        while 1:
            choice=random.randint(0,8)
            if moves[choice] != " ":
                pass
            else:
                moves[choice]=mark
                break
    return choice
def checkWinner(moves):
    status = 0
    player_won=None
    if moves[0] == moves[1] == moves[2] and moves[0] != " ":
        status = 1 
        player_won=moves[0]

    elif moves[3] == moves[4] == moves[5] and moves[3] != " ":
        status = 1 
        player_won=moves[3]

    elif moves[6] == moves[7] == moves[8] and moves[6] != " ":
        status = 1 
        player_won=moves[6]
    
    elif moves[0] == moves[3] == moves[6] and moves[0] != " ":
        status = 1 
        player_won=moves[3]

    elif moves[1] == moves[4] == moves[7] and moves[1] != " ":
        status = 1 
        player_won=moves[1]

    elif moves[2] == moves[5] == moves[8] and moves[2] != " ":
        status = 1 
        player_won=moves[2]

    elif moves[0] == moves[4] == moves[8] and moves[0] != " ":
        status = 1 
        player_won=moves[0]

    elif moves[2] == moves[4] == moves[6] and moves[2] != " ":
        status = 1 
        player_won=moves[2]
    
    return (status, player_won)

def checkDraw(moves):
    draw_status=0
    if moves.count(' ') == 0:
        draw_status=1 
    return draw_status

def saveGame(moves, player_o, player_x):
    gameData=[moves,player_o,player_x]
    saveGameName= input("Enter game name : ")
    filePath=f"./games/{saveGameName}.txt"
    with open(filePath, "w") as f:
        f.write(str(gameData))
        f.close()
    print(f"Game named : {saveGameName} saved successfully! Location: {filePath}")


logo = """

______________________________________________________

   ------------            ---------    ------------
        |          |       |            |          |
        |          |       |            |    ||    |
        |          |       |            |    ||    |
        |          |       |            |    ||    |
        |          |       |            |          |
        |          |       ---------    ------------

______________________________________________________
"""

if __name__=="__main__":
    print(logo)
    isGameLoaded=[0]

    while 1:
        choice =input("New game or load a game?(N/L) : ").replace(" ", "").lower()
        if choice=="n":
            moves=[' ',' ',' ',' ',' ', ' ', ' ', ' ', ' ']
            print("You are [o] and Computer [x]")
            player_o=input("Player [o] name? : ")
            player_x=input("Player [x] name? : ")
            break
        elif choice=="l":
            print("type the gamedata from the save files MANUALLY (im done with this thing and want this thing to be done, i should be studing for my exams and here i am doing this :/ )")
            player_o=input("Player [o] name? : ")
            player_x=input("Player [x] name? : ")
            moves=eval(input("Enter the moves list(as a list) : "))
            print("Saved game:- ")
            boardDraw(moves)
            isGameLoaded=[1]
            break
        else:
            print(f"{choice}: Not a valid option! try again.")

    print(f"\n{player_o} VS {player_x}\n")
    while 1:
        CM=computerMove(moves,"x",isGameLoaded)
        if CM==None:
            pass
        else:
            print(f"\n{player_x} move : {CM+1}")
        boardDraw(moves)
        status,winner= checkWinner(moves)
        if status == 1:
            if winner == "o":
                winner=player_o
            elif winner == "x":
                winner=player_x
            print(f"{winner} WON!")
            exit()
        elif checkDraw(moves) == 1:
            print("GAME IS A DRAW!")
            exit()
        while 1:
            while 1:
                try:
                    player_o_move=int(input("Enter your choice (box number. 1,2,..,9 or use 0 to exit ): "))
                    if player_o_move == 0:
                        saveGame(moves,player_o,player_x)
                        exit()
                    break
                except ValueError:
                    print("Choice must be an Integer. Please try again")
            try:
                if moves[player_o_move-1] != " ":
                    print(f"{player_o_move}: is already taken. Choose a different box.")
                else:
                    moves[player_o_move-1]="o"
                    print(f"Your move : {player_o_move}")
                    break
            except IndexError:
                print(f"{player_o_move}: NOT A VAILD MOVE! Choose a move only from 1-9. Try Again.")
            print(f"\n{player_o} move : {player_o_move}")
            boardDraw(moves)

        status,winner= checkWinner(moves)
        if status == 1:
            if winner == "o":
                winner=player_o
            elif winner == "x":
                winner=player_x
            boardDraw(moves)
            print(f"{winner} WON!")
            exit()

        elif checkDraw(moves) == 1:
            boardDraw(moves)
            print("GAME IS A DRAW!")
            exit()
            
        




