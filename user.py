class adventurer:
    def __init__(self, coins, xp, wood, food):
        self.coins = coins
        self.xp = xp
        self.wood = wood
        self.food = food

global mycoins
global myxp
global mywood
global myfood
global user


mycoins = 5
myxp = 0
mywood = 0
myfood = 4


user = adventurer(mycoins, myxp, mywood, myfood)
import Chapter1
