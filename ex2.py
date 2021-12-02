def main():
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
        temperatura = float(input("|\t\t Introdueix temperatura:\t\t\t\t\t\t\t\t\t|"))
        print("|\t\t_____________________________________________________\t\t|")
        print("|\t\tQuina acció vols fer:\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\tSelecciona una opcio: \t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t1.-Convertir a graus Farenheit \t\t\t\t\t\t\t\t|")
        print("|\t\t2.-Convertir a graus Kelvin \t\t\t\t\t\t\t\t|")
        print("|\t\t3.-Sortir\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t_____________________________________________________\t\t|")
        num = int(input("Introdueix l'opció:"))


        match num:
            case 1:
                print("Opció escollida: Convertir a graus Farenheit.")
                cal = float(temperatura * 1.8000 + 32.00)
                res = round(cal, 2)
                print("Resultat:", end=" ")
                print(res, end=" ")
                print("ºF")
                x = int(input("Vols fer un altre operació: 0.Si 1.No."))
            case 2:
                print("Opció escollida: Convertir a graus Kelvin.")
                cal = float(temperatura + 273.15)
                res = round(cal, 2)
                print("Resultat:", end=" ")
                print(res, end=" ")
                print("ºK")
                x = int(input("Vols fer un altre operació: 0.Si 1.No."))
            case 3:
                print("Opció escollida: Sortir.")
                print("Sortin.....")
                x = 1


if __name__ == '__main__':
    main()
