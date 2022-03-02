
def crear():
    name = input("Introdueix el nom del fitxer que vols crear:")
    f = open(name, "a")
def mostrar():
    name = input("Introdueix el nom del fitxer que vols veure:")
    f = open(name, "r")
    print(f.read())
    f.close()
def escriure():
    name = input("Introdueix el nom del fitxer que vols escriure:")
    f = open(name, "w")
    text = input("Introdueix un text: ")[:100]
    f.write(text)
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
        print("|\t\t2.-Mostrar  \t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t3.-Escriu \t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t4.-Sortir\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t_____________________________________________________\t\t|")
        num = int(input("Introdueix l'opció:"))

        match num:
            case 1:
                crear()
            case 2:
                mostrar()
            case 3:
                escriure()
            case 4:
                print("Opció escollida: Sortir.")
                print("Sortin.....")
                x = 1

