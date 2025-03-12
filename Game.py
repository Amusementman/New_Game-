life_num = 1
def GAME(life_num):
    def lives():
        if life_num > 0:
            redo = input("Would you like to play again? ")
            if redo == "yes":
                GAME()
            else:
                print("Perhaps another time.")
        else:
            print("Bye bye!")
    inventory = ["Dragon egg", ]
    print("Room puzzle")
    awa = input("num?")
    if awa == 1:
        print("Win!")
        lives()
    else:
        life_num = 0
        lives()

GAME(life_num)