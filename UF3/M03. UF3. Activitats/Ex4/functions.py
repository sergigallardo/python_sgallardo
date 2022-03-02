import csv
def inputs():
    num=1
    while num == 1:
        name = input("Introdueix el teu nom:")
        surname = input("Introdueix el teu cognom:")
        age = input("Introdueix la teva edat:")
        selection = int(input("Introdueix la tecnologia en la que estas interessat/da:\n---------------------------------------------\n1.Robotica\n2.Inteligencia artificial\n3.Nanotecnologia\n4.Informatica cuantica\n5.Bioinformática\n-------------------------------------------\nSeleccció:"))
        match selection:
            case 1:
                tecnology = "Robotica"
            case 2:
                tecnology = "Inteligencia articial"
            case 3:
                tecnology = "Nanotecnologia"
            case 4:
                tecnology = "Informatica cuantica"
            case 5:
                tecnology = "Bioinformatica"

        id = (name[:2] + surname[:2] + age)

        with open('register.csv', 'a') as csvfile:
            writeCSV = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writeCSV.writerow([id, name, surname, age, tecnology])
        num = int(input("Vols introduir un altre registre [1=Si/0=No]:"))
