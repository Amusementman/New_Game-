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
    print(life_num)
    print("You groan as you start to open your eyes. You sit up, looking around the room to get an idea of where you are.")
    print("The room your in has metal walls with a strangely soft purple carpet. There's nothing else in the room beside a door across from you, three paintings to your right and a TV in the left corner of the room.")
    print("Suddenly the TV turns on...'Welcome!' a cheery voice says as a dark silouette appears on screen.")
    print("You squint your eyes. 'I know you're probably confused so i'll break your situation down for you'.")
    print("They pause, something unsettles you. 'You're currently in my escape room. All you have to do is complete puzzles and your home free!' Failure to and...there will be consequences. Simple!'")
    print("Now this first puzzle is easy, figure out the right combo of paintings to open the door.")
    print("In the meantime I'll read you a story I wrote. Totally unrelated :)")
    print("The night sky lums over the castle, empty and void. The only living thing in sight is hidden within the walls of a garden. Roses and all sorts of plants surround the inside of the garden.")
    print("Sat sadly on the fountain is a man, the only living thing. He's crying after his wife left him at the alter. With his only company being that of the plants.")
    print("You look over at the paintings as he talks. The first painting is of a flower garden.")
    print("The second painting is of a crying man.")
    print("The third painting is of a night sky.")
    print("The strangers voice cuts and you're left alone.")
    chances = 3
    def puzzle_one(chances, life_num): 
        def chances_a(chances, life_num):
            if chances == 2:
                print("Two chances left")
                chances = 2
                puzzle_one(chances, life_num)
            elif chances == 1:
                print("One chance left")
                chances = 1
                puzzle_one(chances, life_num)
            else:
                print("The screen starts blaring an obnoxious alarm, causing you to cover your ears.")
                print("You can barely hear yourself think until. You think no longer.")
                life_num = life_num - 1
                lives()
        print("You stare at the paintings...there has to be some right combination")
        awa = input("What is the order of paintings? (List based on first = 1, no spaces inbetween them) ")
        if awa == "312":
            print("You flinch as the screen shines a bright green, but luckily for you, you're okay!")
            print("Instead the door opens and you walk through.")
            print("The stranger laughs! 'Fantastic! Fantastic' they cheer.")
            print("You look around, you're in an elevator.")
            print("They seemingly smile.")
            print("'You really did grand', they say, 'and so, I'll let you go'.")
            print("Suddenly the elevator doors open and the outside shines bright.")
            print("You stare in amazement as you step outside.")
            print("You smile to yourself, until you feel a pain in your chest and everything goes black.")
            print("You can faintly hear someone whisper: DFGI")
            life_num = life_num - 1
            lives()
        elif awa == "4679":
            print("Everything stops for a moment. The music cuts, the paintings fall and everything, walls included, fall onto the floor.")
            print("You hear a panicked voice behind you, 'no, no, no, how did they even-UGH!'")
            print("You walk towards the booth where the voice is coming from. You slam open the curtain. Finding a small alligator inside.")
            print("'What?' you ask. The alligator looks around nervously, 'hey man, sorry about the whole game thing...you know what, you did great, just take that exit door and your home free. Promise.'")
            print("You stare at it in confusion before shrugging and heading towards the door.")
            print("You nervously open it and step outside. Loud streets blare out and a cities scenery comes into view.")
            print("Yup, you're safe and you're home now.")
            print("The end...")
        else:
            print("A bright red flashes on the TV screen. Uh oh")
            chances = chances - 1
            chances_a(chances, life_num)
    puzzle_one(chances, life_num)
    

GAME(life_num)