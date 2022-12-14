import os

def resources_path():
    return os.path.join(os.path.split(os.path.dirname(__file__))[0],'resources')

class Player:
    def __init__(self, name, gender, character, Xcoordinates, Ycoordinates,
                 score=0, health=100, alive=True, arrows=3, shutgun=3):
        self.__alive = alive
        self.__name = name
        self.__Xcoordinates = Xcoordinates
        self.__Ycoordinates = Ycoordinates
        self.__gender = gender
        self.__character = character
        self.__health = health
        self.__score = score
        ## arrow for shooting flying dragon
        self.__arrows = arrows
        ## shutguns for shooting walking monsters
        self.__shutgun = shutgun

    ## getter functions ...............
    def GetShutGuns(self):
        return self.__shutgun

    def GetArrows(self):
        return self.__arrows

    def GetHealth(self):
        return self.__health

    def GetScore(self):
        return self.__score

    def GetName(self):
        return self.__name

    def GetLifeStatus(self):
        return self.__alive

    def GetGender(self):
        return self.__gender

    def GetCharacter(self):
        return self.__character

    def GetX(self):
        return self.__Xcoordinates

    def GetY(self):
        return self.__Ycoordinates

    ## setter functions ......................

    ## 1 - incrementing functions
    def ShutGunIncrement(self):
        self.__shutgun += 1
        print("collected, now got shutguns with a total of ", self.__shutgun)

    def ArrowsIncrement(self):
        self.__arrows += 1
        print("collected, now got arrows with a total of ", self.__arrows)

    def ScoreIncrement(self):
        self.__score += 1

    ## let the maximum health be 100
    def HealthIncrement(self):
        self.__health = 100

    ## 2 - decrementing functions
    def ShutgunDecrement(self):
        self.__shutgun -= 1
        print("One shutgun was used, now got shutguns with a total of ",
              self.__shutgun)

    def ArrowsDecrement(self):
        self.__arrows -= 1
        print("One arrow was used, now got arrows with a total of ",
              self.__shutgun)

    def HealthDecrement(self):
        self.__health -= 50

    def ScoreIncrement(self):
        self.__score += 1
        ## more setter functions

    def north(self):
        if (self.__Xcoordinates != 99):
            self.__Xcoordinates += 1
            return True
        else:
            return False

    def south(self):
        if (self.__Xcoordinates != 0):
            self.__Xcoordinates -= 1
            return True
        else:
            return False

    def east(self):
        if (self.__Ycoordinates != 99):
            self.__Ycoordinates += 1
            return True
        else:
            return False

    def west(self):
        if (self.__Ycoordinates != 0):
            self.__Ycoordinates -= 1
            return True
        else:
            return False

    def Game_Over(self):
        self.__alive = False
        with open(os.path.join(resources_path(), "GameOver.txt"), encoding='utf-8') as f:
            for i in range(12):
                print(f.readline(), end='')
            print('\n')
        print("Game is over !")
