# miguel jusino
# main player and all that I want to go with him through chapters
from user import user
def game():
    print("Chapter 1 start!")
    print("You have ", user.coins, " coins")
    print("You have ", user.xp, " XP")
dance = input("Do you want to keep dancing? Y/N")
#     #go = str(input("continue game"))

while dance == "Y":
        print("more coins!")
        user.coins += 5
        print("You have ", user.coins, " coins!")
        dance = input("Continue dancing? Y/N")

print("on to the next level")
    # import Chapter2


