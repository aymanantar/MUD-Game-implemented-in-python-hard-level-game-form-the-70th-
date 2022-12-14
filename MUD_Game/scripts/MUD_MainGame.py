import os,random, pandas as pd
from .player import Player 
from .board import Board


def resources_path():
    return os.path.join(os.path.split(os.path.dirname(__file__))[0],'resources')

## saving the game (number of players ,)...............
def Save(n, arr):
    df = pd.DataFrame(
        columns=["name", "gender", "character", "Xcoordinates", "Ycoordinates",
                 "score", "health", "alive", "arrows", "shutguns"])
    for i in range(0, n):
        ##   name, gender, character, Xcoordinates, Ycoordinates, score , health , alive, arrows, shutgun 
        df2 = pd.DataFrame.from_dict(
            {"name": [arr[i].GetName()], "gender": [arr[i].GetGender()],
             "character": [arr[i].GetCharacter()],
             "Xcoordinates": [arr[i].GetX()], "Ycoordinates": [arr[i].GetY()],
             "score": [arr[i].GetScore()], "health": [arr[i].GetHealth()],
             "alive": [arr[i].GetLifeStatus()], "arrows": [arr[i].GetArrows()],
             "shutguns": [arr[i].GetShutGuns()]})
        df = pd.concat([df, df2], ignore_index=True)
    while (True):
        print("Enter the target file")
        FileName = input()
        try:
            df.to_csv(os.path.join(resources_path(), FileName) + ".csv")
            print("Saved Successfully")
            break
        except:
            print("worng file name, try again")

## game starting .....
def StartGame():
    ## loading players  .......................    
    while (True):
        ## number of players
        n = 1
        ## array of 'Player' object
        players = []
        print(" 1- Play a new game \n 2- Load a game \n 3- exit")
        choice = int(input())
        ## new game creating
        if (choice == 1):
            ## pinting the game entry Image.
            ## entry image printing ............
            with open(os.path.join(resources_path(), "entry.txt"), encoding='utf-8') as f:
                for i in range(12):
                    print(f.readline(), end='')
                print('\n')
            while (True):
                print(" Enter the number of players")
                try:
                    n = int(input())
                    break
                except:
                    print("not a valid number, try again")
            for i in range(0, n):
                print("you are player number ", i + 1)
                print("Hey Beast, what’s your name?")
                name = input()
                print("___ \n", " Welcome", "to the world of Warriors, ", name,
                      '.')
                while (True):
                    print("Select your Gender (Male / Female)")
                    gender = input()
                    if (gender == "Male"):
                        print(
                            "___ \n Choose your Character (Tuleca, Marok, Hellama, or other...)")
                        character = input()
                        break
                    elif (gender == "Female"):
                        print(
                            "___ \n Choose your Character (Shujia, Lia Sina, Mia Yi, or other...)")
                        character = input()
                        break
                    else:
                        print("Wrong gender was picked, try again")
                ## construncting player object to load it in the array
                player = Player(name, gender, character, random.randint(0, 99),
                                random.randint(0, 99))
                players.append(player)
            break

        elif (choice == 2):
            ## exsiting game loading
            ## pinting the game entry Image.
            ## entry image printing ............
            with open(os.path.join(resources_path(), "entry.txt"), encoding='utf-8') as f:
                for i in range(12):
                    print(f.readline(), end='')
                print('\n')
            while (True):
                print("Enter the target file")
                FileName = input()
                try:
                    df = pd.read_csv(os.path.join(resources_path(), FileName) + ".csv")
                    break
                except:
                    print("worng file name, try again")
            n = len(df)
            for i in range(0, n):
                ##constructing player bocject wiht : name, gender, character, Xcoordinates, Ycoordinates, score , health , alive, arrows, shutgun 
                player = Player(df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3],
                                df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6],
                                df.iloc[i, 7], df.iloc[i, 8], df.iloc[i, 9],
                                df.iloc[i, 10])
                ## push the player object in the list 
                players.append(player)
            break
        elif (choice == 3):
            exit("good bye")
        else:
            print("wrong input, try again ")
    ## starting the game ........................
    for i in range(0, n):
        ## checking if we should start with this player or moving to the next one (in case of a loaded game from csv files)
        if (players[i].GetLifeStatus() == True):
            print("This turn is for ", players[i].GetName())
        ## constructing a new random board
        board = Board()
        while (players[i].GetLifeStatus() == True):
            cell = board.GetCell(players[i].GetX(), players[i].GetY())
            board.Empty(players[i].GetX(), players[i].GetY())
            if (cell == "."):
                print("This Cell is empty")
            elif (cell == "camps"):
                board.camp(players[i])
            elif (cell == "monster"):
                board.monster(players[i])
            elif (cell == "heal"):
                board.heal(players[i])
            elif (cell == "arrow"):
                board.arrow(players[i])
            elif (cell == "shutgun"):
                board.shutgun(players[i])
            elif (cell == "hole"):
                board.hole(players[i])
            elif (cell == "fireball"):
                board.fireball(players[i])
            elif (cell == "dragon"):
                board.dragon(players[i])
                ## still alive ??  to the next move ..................
            while (players[i].GetLifeStatus() == True):
                print(
                    " Choose the dirction of your next move ('north', 'east', 'south', and 'west' )  \n you can also press 'S' to save and exit the game :")
                dirction = input()
                if (dirction == 'S'):
                    Save(n, players)
                    print("good bye")
                    exit()
                elif (dirction == "north"):
                    if (players[i].north()):
                        break
                    else:
                        print(
                            "You are on the edge! north, is not allowed form your cell")
                elif (dirction == "east"):
                    if (players[i].east()):
                        break
                    else:
                        print(
                            "You are on the edge! east, is not allowed form your cell")
                elif (dirction == "south"):
                    if (players[i].south()):
                        break
                    else:
                        print(
                            "You are on the edge! south, is not allowed form your cell")
                elif (dirction == "west"):
                    if (players[i].west()):
                        break
                    else:
                        print(
                            "You are on the edge! west, is not allowed form "
                            "your cell")
                else:
                    print(" Wrong dirction, try again")
        ## Geme has ended, now creating The leader board and saving it 

    ## sorting function with the priority for the highest score to be in the begining
    def srt(player):
        return -player.GetScore()

    players.sort(key=srt)
    ## display the leaderboard ..........
    print("Leader board .................................")
    for i in range(0, n):
        print("in the ", i + 1, "th place : ", players[i].GetName(),
              " With total score of : ", players[i].GetScore())
    ## save and end .....
    Save(n, players)

