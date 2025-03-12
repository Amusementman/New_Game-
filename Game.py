life_num = 5
def GAME(life_num):
    def lives():
        if life_num > 0:
            redo = input("Would you like to play again? ")
            if redo == "yes":
                GAME(life_num)
            else:
                print("Perhaps another time.")
        else:
            print("Bye bye!")
    inventory = [""]
    print(life_num)
    print("You groan as you start to open your eyes. You sit up, looking around the room to get an idea of where you are.")
    print("The room your in has metal walls with a strangely soft purple carpet. There's nothing else in the room beside a door across from you, three paintings to your right and a TV in the left corner of the room.")
    print("Suddenly the TV turns on...'Welcome!' a cheery voice says as a dark silouette appears on screen.")
    print("You squint your eyes. 'I know you're probably confused so i'll break your situation down for you'.")
    print("They pause, something unsettles you. 'You're currently in my escape room. All you have to do is complete puzzles and your home free!' Failure to and...there will be consequences. Simple!'")
    print("Now this first puzzle is easy, figure out the right combo of paintings to open the door.")
    print("In the meantime I'll read you a poem I wrote.")
    print("Insert poem prt.1")
    print("You look over at the paintings as he talks. The first painting is of a flower garden.")
    print("Insert poem prt. 2")
    print("The second painting is of a crying man.")
    print("insert poem prt. 3")
    print("The third painting is of a night sky.")
    print("The strangers voice cuts and you're left alone.")
    chances = 3
    def puzzle_one(chances): 
        def chances_a(chances, life_num):
            if chances == 2:
                print("Two chances left")
                chances = 2
                puzzle_one(chances)
            elif chances == 1:
                print("One chance left")
                chances = 1
                puzzle_one(chances)
            else:
                print("The screen starts blaring an obnoxious alarm, causing you to cover your ears.")
                print("You can barely hear yourself think until. You think no longer.")
                life_num = life_num - 1
                lives()
        print("You stare at the paintings...there has to be some right combination")
        awa = input("What is the order of paintings? (List based on first = 1, no spaces inbetween them) ")
        if awa == "312":
            def puzzle_two():
                print("You flinch as the screen shines a bright green, but luckily for you, you're okay!")
                print("Instead the door opens and you walk through.")
                print("The stranger laughs! 'Fantastic! Fantastic' they cheer, 'I hope your prepared for the next puzzle!'.")
                print("Just as they say that, the lights go out and you can feel the whole room move around you.")
                print("Once the lights go on, you realize your in an elevator.")
            puzzle_two()
        else:
            print("A bright red flashes on the TV screen. Uh oh")
            chances = chances - 1
            chances_a(chances, life_num)
    puzzle_one(chances)
    

GAME(life_num)