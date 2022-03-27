import csv
from datetime import datetime
import pandas as pd


def create():
    file = 'files/register.csv'
    file2 = 'files/ambient.csv'
    f = open(file, "a")
    f = open(file2, "a")
    print("Arxiu creat: OK. Ruta:/" + file)
    print("Arxiu creat: OK. Ruta:/" + file2)

    val = 'Si'
    return val

def checkFileExistance():
    try:
        with open("files/register.csv", 'r') as f:#Proba obrir el arxiu
            val = 'Si' #Si el arxiu existeix dona valor 'Si' a 'val'.

    except FileNotFoundError as e:
           val = 'No' #Si el arxiu no existeix dona valor 'No' a 'val'.

    except IOError as e:
            val = 'No' # Si dona el Error: IOError donara a 'val'  el valor de 'No'.
    return val  #Retorna 'val' que val te la funcio de al hora de registrar els inputs posar capçelera o no al arxiu CSV.

def read():
    df = pd.read_csv("files/register.csv")
    print(df)
def intervals(interval):
    if (interval == 0):
        min = '00'
        return min
    if (interval == 1):
        min = '10'
        return min
    if (interval == 2):
        min = '20'
        return min
    if (interval == 3):
        min = '30'
        return min
    if (interval == 4):
        min = '40'
        return min
    if (interval == 5):
        min = '50'
        return min
    if (interval == 6):
        min = '00'
        return min

def ambient_classe(curs, aula, date, hour1, hour2, val):
    ambient = dict()
    # Demana nivell de CO2 , Temperatura, Humitat.
    interval = 0
    x=7
    while interval < x:
        ambient['curs'] = curs
        ambient['aula'] = aula
        ambient['dia'] = date
        min = intervals(interval)
        if(interval == 6):
            hour1 = hour2
        hour = hour1 + ':' + min
        ambient['hora'] = hour
        ambient['nivell_co2'] = input("Introdueix el nivell de CO2 actual" + "[Hora actual:" + hour + "]" + ":\n=>")
        ambient['tempertatura'] = input("Introdueix la temperatura actual" + "[Hora actual:" + hour + "]" + ":\n=>")
        ambient['humitat'] = input(
            "Introdueix el nivell de humitat actual" + "[Hora actual:" + hour + "]" + ":\n=>")
        interval = interval + 1
        with open('files/ambient.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['curs', 'aula', 'dia', 'hora_1', 'nivell_co2', 'temperatura', 'humitat']
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if val == 'Si':
                writeCSV.writeheader()  # Se encarrega que de escriure la capçalera del CSV.
                val = 'Capçelera'

                try:
                    writeCSV.writerow(ambient)
                except:
                    print("No s'ha pogut inserir el registre.")
                else:
                    print("El registre s'ha inserit correctament.")







def inputs():
    val = checkFileExistance()
    if (val == 'No'):
        create()
        val = 'Si'
    else:
        val = 'Capçelera'

    regist = dict()
    regist['curs'] = input("Introdueix el Curs:\n=>")
    curs = regist['curs']
    regist['aula'] = input("Introdueix el Numero de Aula:\n=>")
    aula =  regist['aula']
    regist['num_alumnes'] = int(input("Introdueix el numero de alumnes:\n=>"))
    regist['num_professors'] = int(input("Introdueix el numero de professors:\n=>"))
    while True:
        try:
            date_str = input('\n Introdueix la data  ==> exemple "18/01/1952"...:\n=> ')
            date = datetime.strptime(date_str, '%d/%m/%Y')
            break
        except:
            print("\n La data introduida no es correcta...")
    regist['dia'] = date

    print("|\t\t_____________________________________________________\t\t|")
    print("|\t\t Indica a quina hora es la classe:\t\t\t\t\t\t\t\t\t|")
    print("|\t\t1.-8:00-9:00. \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t2.-9:00-10:00.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t3.-10:00-11:00.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t4.-11:30-12:30.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t5.-12:30-13:30.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t6.-13:30-14:30.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t7.-17:30-18:30.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t8.-18:30-19:30.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t9.-19:30-20:30.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t_____________________________________________________\t\t|")
    num = int(input("Introdueix l'opció:\n=>"))
    while (num < 1 or num > 9):
        num = int(input("Error!Introdueix l'opció:\n=>"))
    match num:
        case 1:
            aux = '8:00-9:00'
            hour1 = '8'
            hour2 = '9'
        case 2:
            aux = '9:00-10:00'
            hour1 = '9'
            hour2 = '10'
        case 3:
            aux = '10:00-11:00'
            hour1 = '10'
            hour2 = '11'
        case 4:
            aux = '11:30-12:30'
            hour1 = '11'
            hour2 = '12'
        case 5:
            aux = '12:30-13:30'
            hour1 = '12'
            hour2 = '13'
        case 6:
            aux = '13:30-14:30'
            hour1 = '13'
            hour2 = '14'

        case 7:
            aux = '17:30-18:30'
            hour1 = '17'
            hour2 = '18'
        case 8:
            aux = '18:30-19:30'
            hour1 = '18'
            hour2 = '19'
        case 9:
            aux = '19:30-20:30'
            hour1 = '19'
            hour2 = '20'

    regist['hora_classe'] = aux
    regist['nom_professor'] = input("Introdueix el nom del professor:\n=>")
    regist['assignatura'] = input("Introdueix el nom de la assignatura:\n=>")
    # Demana nivell de CO2 , Temperatura, Humitat.

    regist['temps_porta_principal_oberta'] = int(input("Introdueix en minuts quant temps ha estat la porta principal oberta:\n=>"))
    print("|\t\t_____________________________________________________\t\t|")
    print("|\t\t La classe disposa d una porta secundaria:\t\t\t\t\t\t\t\t\t|")
    print("|\t\t1.-Si. \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t2.-No.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t_____________________________________________________\t\t|")
    num = int(input("Introdueix l'opció:\n=>"))
    while (num < 1 or num > 2):
        num = int(input("Error!! Introdueix l'opció:\n=>"))
    match num:
        case 1:
            second = 'Si'
            temps = int(input('Quant temps ha estat la porta secundaria oberta durant la classe[temps en minuts]:\n=>'))
        case 2:
            second = 'No'
            temps = 'NULL'

    regist['porta_secundaria'] = second
    regist['temps_porta_sec'] = temps

    print("|\t\t_____________________________________________________\t\t|")
    print("|\t\t Indica quin tipus de finestres tens al aula:\t\t\t\t\t\t\t\t\t|")
    print("|\t\t1.-Finestres externes. \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t2.-Finestres internes.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t_____________________________________________________\t\t|")
    num = int(input("Introdueix l'opció:\n=>"))
    while (num < 1 or num > 2):
        num = int(input("Error!! Introdueix l'opció:\n=>"))
    match num:
        case 1:
            aux = 'Externes'
        case 2:
            aux = 'Internes'
    regist['finestres'] = aux

    print("|\t\t_____________________________________________________\t\t|")
    print("|\t\tEn algun moment ha hagut ventilacio creuada:\t\t\t\t\t\t\t\t\t|")
    print("|\t\t1.-Si. \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t2.-No.  \t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t_____________________________________________________\t\t|")
    num = int(input("Introdueix l'opció:\n=>"))
    while (num < 1 or num > 2):
        num = int(input("Error!! Introdueix l'opció:\n=>"))
    match num:
        case 1:
            creu = 'Si'
        case 2:
            creu = 'No'
    regist['v_creuada'] = creu

    ambient_classe(curs, aula, date, hour1, hour2, val)

    #Inici de insercio de registres al arxiu csv.
    with open('files/register.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['curs', 'aula', 'num_alumnes', 'num_professors', 'dia', 'hora_classe', 'nom_professor', 'assignatura', 'temps_porta_principal_oberta', 'porta_secundaria', 'temps_porta_sec', 'finestres', 'v_creuada']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if val == 'Si':
            writeCSV.writeheader()  # Se encarrega que de escriure la capçalera del CSV.
            val = 'Capçelera'
        try:
            writeCSV.writerow(regist)
        except:
            print("No s'ha pogut inserir el registre.")
        else:
            print("El registre s'ha inserit correctament.")




def benviguda():
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
    menu()

def menu():
    x = 0
    while x != 1:
        print("|\t\t_____________________________________________________\t\t|")
        print("|\t\tQuina acció vols realitzar:\t\t\t\t\t\t\t\t\t|")
        print("|\t\t1.-Registra  \t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t2.-Mostra \t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t3.-Sortir\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t_____________________________________________________\t\t|")

        num = int(input("Introdueix l'opció:\n=>"))
        while(num<1 or num>4):
            num = int(input("Error!! Introdueix l'opció:\n=>"))
        match num:
            case 1:
                inputs()
            case 2:
                read()
            case 3:
                print("Opció escollida: Sortir.")
                print("Sortin.....")
                x = 1
