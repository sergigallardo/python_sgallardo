import csv


def get_info():
    line_count = 0
    woman = 0
    with open('creussj.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile)
        for row in readCSV:
            if  row['Sexe'] == 'Dona': #Condicional per sol comptar els registres amb el 'Sexe' = 'Dona'.
                woman +=1
            line_count += 1 #compte els numero de lineas/registres/projectes del arxiu CSV.
    print(f"El document conté {line_count} registres i te un total de {woman} Dones")