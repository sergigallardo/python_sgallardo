import csv
def inputs():
    num=1
    while num == 1:
        name = input("Introdueix el teu nom:")
        surname = input("Introdueix el teu cognom:")
        age = input("Introdueix la teva edat:")
        tecnology = input("Introdueix la tecnologia en la que estas interessat/da:")
        id = (name[:2] + surname[:2] + age)

        with open('register.csv', 'a') as csvfile:
            writeCSV = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writeCSV.writerow([id, name, surname, age, tecnology])
        num = int(input("Vols introduir un altre registre [1=Si/0=No]:"))
