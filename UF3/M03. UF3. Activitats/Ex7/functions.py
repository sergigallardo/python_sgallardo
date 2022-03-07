import csv
import pandas as pd
from datetime import datetime
def inputs():
    y = int(0)
    num = int(input("Quants registres vols introduir:"))
    while y < num:
        dictionary = dict()
        while True:
            try:
                date_str = input('\n Introdueix la data de publicació ==> exemple "18/01/1952"...: ')
                date = datetime.strptime(date_str, '%d/%m/%Y')
                break
            except:
                print("\n La data introduida no es correcta...")
        dictionary['date'] = date
        dictionary['name'] = input("Introdueix el nom de la exemplar trobat: ")
        dictionary['local'] = input("Introdueix el nom de la localització: ")
        dictionary['type'] = input("Introdueix el tipus de especie: ")
        dictionary['mid'] = int(input("Introdueix la mida del exemplar: "))
        dictionary['description'] = input("Introdueix una descripció del exemplar: ")
        with open('bio.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['date', 'name', 'local', 'type', 'mid', 'description']
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
    df = pd.read_csv('bio.csv')
    print(df)

def menu():
    x = 0
    while x != 1:
        print("|\t\t_____________________________________________________\t\t|")
        print("|\t\tQuina acció vols realitzar:\t\t\t\t\t\t\t\t\t|")
        print("|\t\t1.-Registra \t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t2.-Mostrar  \t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t3.-Sortir\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t_____________________________________________________\t\t|")
        num = int(input("Introdueix l'opció:"))

        match num:
            case 1:
                inputs()
            case 2:
                read()
            case 3:
                print("Opció escollida: Sortir.")
                print("Sortin.....")
                x = 1