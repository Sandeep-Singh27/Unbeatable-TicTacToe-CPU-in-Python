import os
while True: 
    os.system("cls")   
    print("LET'S START GAME:-")
    print()
    print("WHO WILL PLAY FIRST?","PRESS 1 FOR PLAYER","PRESS 2 FOR CPU",sep="\n")
    choice = int(input("CHOICE: "))

    if choice == 1:
        import PlayerFirst
        break
    elif choice == 2:
        import CpuFirst
        break
    else:
        print("Wrong Choice Try Again...")