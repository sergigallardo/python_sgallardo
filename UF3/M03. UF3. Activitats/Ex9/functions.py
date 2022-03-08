import csv
from datetime import datetime
import random
import pandas as pd

def inputs():
    y= int(0)
    num = int(input("Quants registres vols introduir:"))
    dictionary = dict()
    while y < num:
        dictionary['id'] = random.randint(0, 50000)
        dictionary['group'] = input("Introdueix el nom del grup/cantant:")
        dictionary['singel'] = input("Introdueix el nom de la canço:")
        while True:
            try:
                date_str = input('\n Introdueix la data de publicació ==> exemple "18/01/1952"...: ')
                date = datetime.strptime(date_str, '%d/%m/%Y')
                break
            except:
                print("\n La data introduida no es correcta...")
        dictionary['date'] = date
        dictionary['visual'] = int(input("Introdueix el numero de visualitzacions:"))
        with open('register.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['id', 'group', 'singel', 'date', 'visual']
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writeCSV.writeheader()
            try:
                writeCSV.writerow(dictionary)
            except:
                print("No s'ha pogut inserir el registre.")
            else:
                print("El registre s'ha inserit correctament.")
        y = y + 1
def read():
    df = pd.read_csv("register.csv")
    print(df)
def menu():
    x = 0
    y = 0
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
        print("|\t\t1.-Registra \t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t2.-Mostrar  \t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t3.-Sortir\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t_____________________________________________________\t\t|")
        num = int(input("Introdueix l'opció:"))

        match num:
            case 1:
                print("Opció escollida: Registra.")
                inputs()
            case 2:
                print("Opció escollida: Mostrar.")
                read()
            case 3:
                print("Opció escollida: Sortir.")
                print("Sortin.....")
                x = 1