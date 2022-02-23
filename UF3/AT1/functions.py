def read():
    name = input("Introdueix el nom del arxiu que vols llegir:") + ".txt"
    f = open(name, "r")
    print(f.readlines())
    f.close()


def create():
    name = input("Introdueix el nom del arxiu que vols crear:") + ".txt"
    f = open( name , "w")
    f.close()
def write():
    name = input("Introdueix el nom del arxiu en el que vols escriure:") + ".txt"
    f = open(name, "w")
    write = input("Introdueix un text:")
    f.write(write)
    f.close()

def menu():
    x = 0
    while x != 1:
        print("_____________________________________________________________________")
        print("|\t\t                                                     \t\t|")
        print("|\t\t______                 _                   _     _ _ \t\t|")
        print("|\t\t| ___ \               (_)                 | |   | | |\t\t|")
        print("|\t\t| |_/ / ___ _ ____   ___ _ __   __ _ _   _| |_  | | |\t\t|")
        print("|\t\t| ___ \/ _ \ '_ \ \ / / | '_ \ / _` | | | | __| | | |\t\t|")
        print("|\t\t| |_/ /  __/ | | \ V /| | | | | (_| | |_| | |_  |_|_|\t\t|")
        print("|\t\t\____/ \___|_| |_|\_/ |_|_| |_|\__, |\__,_|\__| (_|_)\t\t|")
        print("|\t\t                                __/ |                \t\t|")
        print("|\t\t                               |___/                 \t\t|")
        print("|\t\t_____________________________________________________\t\t|")
        print("|\t\tQuina acció vols realitzar:\t\t\t\t\t\t\t\t\t|")
        print("|\t\t1.-Crear arxiu \t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t2.-Escriure \t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t3.-Llegeix \t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t4.-Sortir\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t_____________________________________________________\t\t|")
        num = int(input("Introdueix l'opció:"))

        match num:
            case 1:
                create()
            case 2:
                write()
            case 3:
                read()
            case 4:
                print("Opció escollida: Sortir.")
                print("Sortin.....")
                x = 1
