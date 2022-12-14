import random
class Board:
    def __init__(self):
        ## initalizing (100*100) board wiht '.'
        self.board = []
        for j in range(0, 100):
            col = []
            for i in range(0, 100):
                col.append(".")
            self.board.append(col)
        ## filling the board randomly with ( 2000 camps , 2500 healing up kits, 1000 shutguns , 1000 arrows , 500 monsters , 500 dragons , 500 holes , 500 fireballs , the rest are empty cells "." )
        for i in range(0, 2000):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            ## ensuring not to take another object's cell         
            while (self.board[x][y] != "."):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
            self.board[x][y] = "camps"
        for i in range(0, 2500):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            ## ensuring not to take another object's cell             
            while (self.board[x][y] != "."):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
            self.board[x][y] = "heal"
        for i in range(0, 1000):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            ## ensuring not to take another object's cell         
            while (self.board[x][y] != "."):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
            self.board[x][y] = "arrow"
        for i in range(0, 1000):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            ## ensuring not to take another object's cell             
            while (self.board[x][y] != "."):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
            self.board[x][y] = "shutgun"
        for i in range(0, 500):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            ## ensuring not to take another object's cell             
            while (self.board[x][y] != "."):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
            self.board[x][y] = "hole"
        for i in range(0, 500):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            ## ensuring not to take another object's cell         
            while (self.board[x][y] != "."):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
            self.board[x][y] = "fireball"
        for i in range(0, 500):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            ## ensuring not to take another object's cell             
            while (self.board[x][y] != "."):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
            self.board[x][y] = "monster"
        for i in range(0, 500):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            ## ensuring not to take another object's cell 
            while (self.board[x][y] != "."):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
            self.board[x][y] = "dragon"

    def camp(self, player):
        print("opponent dungeon camp was found ")
        while (True):
            print(" 1- bomb it \n 2- leave it ")
            try:
                choice = int(input())
                if (choice == 1):
                    player.ScoreIncrement()
                    print(
                        "Great work ! you destroyed it and gained a gold coin")
                    break
                elif (choice == 2):
                    break
                else:
                    print("worng answer, try again")
            except:
                print("worng answer, try again")

    def heal(self, player):
        print("a healing kit was found ")
        while (True):
            print(" 1- Applay it \n 2- leave it ")
            try:
                choice = int(input())
                if (choice == 1):
                    print("your health is maximum now (100 points)")
                    player.HealthIncrement()
                    break
                elif (choice == 2):
                    break
                else:
                    print("worng number picked, try again")
            except:
                print("worng number picked, try again")

    def shutgun(self, player):
        print("A shutgun was found ")
        while (True):
            print(" 1- Pick it \n 2- leave it ")
            try:
                choice = int(input())
                if (choice == 1):
                    player.ShutGunIncrement()
                    break
                elif (choice == 2):
                    break
                else:
                    print("not a valid number, try again")
            except:
                print("not a valid number, try again")

    def arrow(self, player):
        print("An arrow was found")
        while (True):
            print(" 1- Pick it \n 2- leave it ")
            try:
                choice = int(input())
                if (choice == 1):
                    player.ArrowsIncrement()
                    break
                elif (choice == 2):
                    break
                else:
                    print("not a valid number, try again")
            except:
                print("not a valid number, try again")

    def hole(self, player):
        print("Ops! we fell in a hole and  lost 50 health point ")
        player.HealthDecrement()
        if (player.GetHealth() == 0):
            print("your healt is 0 now, you will die")
            player.Game_Over()

    def fireball(self, player):
        print("Ops! we crashed with a fireball and lost 50 health point ")
        player.HealthDecrement()
        if (player.GetHealth() == 0):
            print("your healt is 0 now, you will die")
            player.Game_Over()

    def monster(self, player):
        print("We are facing a monster right now and you have ",
              player.GetShutGuns(), " Shutguns, and ", player.GetArrows(),
              " Arrows")
        while (True):
            print("Choose your weapon ( arrow or shutgun ) ")
            choice = input()
            if (choice == "shutgun"):

                if (player.GetShutGuns() == 0):
                    print("you have no shutguns! he will kill you ")
                    player.Game_Over()
                    break
                else:
                    print("Great ! we killed him  ")
                    player.ShutgunDecrement()
                    break

            elif (choice == "arrow"):
                print(
                    "You can't kill the monster wiht an arrow , he wil kill you")
                player.Game_Over()
                break
            else:
                print("Wrong choice, try again")

    def dragon(self, player):
        print("We are facing a dragon right now and you have ",
              player.GetShutGuns(), " Shutguns, and ", player.GetArrows(),
              " Arrows")
        while (True):
            print("Choose your weapon ( arrow or shutgun ) ")
            choice = input()
            if (choice == "arrow"):

                if (player.GetArrows() == 0):
                    print("you have no arrows! he will eat you ")
                    player.Game_Over()
                    break
                else:
                    print("Great ! we killed him  ")
                    player.ArrowsDecrement()
                    break

            elif (choice == "shutgun"):
                print(
                    "You can't kill the dragon wiht a shutgun , he wil eat you")
                player.Game_Over()
                break
            else:
                print("Wrong choice, try again")

    def GetCell(self, x, y):
        return self.board[x][y]

    def Empty(self, x, y):
        self.board[x][y] = "."

    def display(self):
        for i in range(0, 99):
            for j in range(0, 99):
                print(self.board[i][j], end=' ')
            print('\n')
