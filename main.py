from termcolor import colored
from os import listdir
from os.path import isdir

move = [
    ['□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '□', '□']
]

move_column = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,

}

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
player1 = "○"
player2 = "x"


def drawBoard(move):
    print(colored("  a b c d e f g", "yellow", attrs=["bold"]))
    k = 1
    for i in move:
        t = colored(k, "yellow", attrs=["bold"])
        k += 1
        tmp = f"{t} "
        for j in i:
            if j == "□":
                data = colored(j, "green", attrs=['bold'])
            elif j == "○":
                data = colored(j, "red", attrs=['bold'])
            elif j == "x":
                data = colored(j, "blue", attrs=['bold'])

            tmp += f"{data} "
        print(tmp)


def checkWinner(move):
    winner = None
    t = 0
    for i in move:
        try:
            for j in range(len(i)):
                if i[j] == player1:
                    if player1 == i[j+1] == i[j+2] == i[j+3]:
                        winner = player1
                        break
                    elif player1 == move[t+1][j] == move[t+2][j] == move[t+3][j]:
                        winner = player1
                        break
                    elif player1 == move[t+1][j+1] == move[t+2][j+2] == move[t+3][j+3]:
                        winner = player1
                        break
                    elif player1 == move[t+1][j-1] == move[t+2][j-2] == move[t+3][j-3]:
                        winner = player1
                        break
                elif i[j] == player2:
                    if player2 == i[j+1] == i[j+2] == i[j+3]:
                        winner = player2
                        break
                    elif player2 == move[t+1][j] == move[t+2][j] == move[t+3][j]:
                        winner = player2
                        break
                    elif player2 == move[t+1][j+1] == move[t+2][j+2] == move[t+3][j+3]:
                        winner = player2
                        break
                    elif player2 == move[t+1][j-1] == move[t+2][j-2] == move[t+3][j-3]:
                        winner = player2
                        break
        except IndexError:
            pass
        t += 1

    return winner


def checkDraw(move):
    isDraw = False
    t = 0
    for i in move:
        if i.count('□') == 0:
            t += 1
    if t == 7:
        isDraw = True
    return isDraw


def playerMove(player, playerName):
    while 1:
        player_move = input(
            f"{playerName} Enter your move : ").replace(" ", "").lower()
        try:
            j = move_column[player_move[0]]
            try:
                if int(player_move[1]) == 0:
                    print(f"{player_move[1]}: Invaild row choice")
                    continue
                else:
                    i = int(player_move[1]) - 1

                if move[i][j] == "□":
                    move[i][j] = player
                else:
                    print("Box is already occupied.")
                winner = checkWinner(move)
                if winner is not None:
                    drawBoard(move)
                    print(f"{winner} won!!")
                    exit()
                if checkDraw(move) is True:
                    print("Game is a draw!")
                    exit()
                break
            except IndexError:
                print(f"{player_move[1]}: Invaild row choice")
        except KeyError:
            print(f"{player_move[0]}: Invaild column choice. ")


def closing(moves, playerName1, playerName2, isGameLoaded, FileName, isPlayer1Turn, isPlayer2Turn):
    if input("do you want to save the game? [y/N] ").lower().replace(" ", "") == "y":
        while 1:
            if isdir("./data/"):
                try:
                    if isGameLoaded[0] == 0:
                        FileName = input("Enter the ganem's name : ")
                    file_path = f"./data/{FileName}"
                    data = [playerName1, playerName2,
                            moves, isPlayer1Turn, isPlayer2Turn]
                    with open(file_path, 'w') as f:
                        f.write(str(data))
                        f.close()
                    print(f"Saved game as {file_path}. Quiting...")
                    exit()

                except Exception as e:
                    print(e)
                    print("Invaild file name. Choose something else.")
            else:
                print("\"data\" directory doesn't exist")
                exit()
    else:
        exit()


def run():
    global move
    isGameLoaded = [0]
    filename = ''
    isPlayer1Turn = True
    isPlayer2Turn = True
    try:
        while True:
            choice = input(
                "Do you want to start a New game or load a game or q to quit ?[n/o/q] : ").replace(" ", "").lower()
            if choice == "n":
                playerName1 = input("Enter your name : ")
                playerName2 = input("Enter the opponent's name : ")
                if (input(f"Your name : {playerName1} and Opponent's {playerName2}. Want to continue? [Y\\n] : ").lower().replace(" ", "")) != "n":
                    break
                else:
                    pass
            elif choice == "o":
                isGameLoaded[0] = 1
                while 1:
                    if isdir("./data/"):
                        try:
                            games = listdir("./data/")
                            for i in range(len(games)):
                                print(f"{i+1} : {games[i]}")
                            try:
                                choice = int(
                                    input("Choose the game [1, 2, 3.. or 0 to exit] : "))
                            except ValueError:
                                print("Choice must be an integer.")
                                continue
                            gameFile = f"./data/{games[choice-1]}"
                            filename = games[choice - 1]
                            with open(gameFile, 'r') as f:
                                gameData = f.readlines()[0]
                                f.close()
                            gameData = eval(gameData)
                            playerName1 = gameData[0]
                            playerName2 = gameData[1]
                            move = gameData[2]
                            isPlayer1Turn = gameData[3]
                            isPlayer2Turn = gameData[4]
                            break

                        except IndexError:
                            print("Not a vaild choice. Choose something else")
                    else:
                        print("\"data\" directory doesn't exits.")
                        exit()
                break
            elif choice == "q":
                exit()
            else:
                print(f"{choice} not a vaild option. (use ^C or q to quit )")
    except KeyboardInterrupt:
        exit()
    print("(type moves like a1, b5, d6, etc and use ^C to exit)\n")
    while 1:
        try:
            if isPlayer1Turn:
                drawBoard(move)
                playerMove(player1, playerName1)
            else:
                isPlayer1Turn = True
        except KeyboardInterrupt:
            closing(move, playerName1, playerName2, isGameLoaded,
                    filename, isPlayer1Turn=True, isPlayer2Turn=True)
        try:
            if isPlayer2Turn:
                drawBoard(move)
                playerMove(player2, playerName2)
            else:
                isPlayer2Turn = True
        except KeyboardInterrupt:
            closing(move, playerName1, playerName2, isGameLoaded,
                    filename, isPlayer1Turn=False, isPlayer2Turn=True)


if __name__ == "__main__":
    print(logo)
    run()
