import csv


def inputs():
    y = int(0)
    capçelera = input("Vols introduir una capçelera al arxiu CSV[si/no]:")
    num = int(input("Quants registres vols introduir:"))
    dictionary = dict()
    while y < num:
        dictionary['year'] = int(input("Introdueix el any:"))
        dictionary['name'] = input("Introdueix el teu nom i cognoms:")
        dictionary['pe'] = input("Personalitat o entitat:")
        dictionary['gender'] = input("Introdueix el teu genere:")
        dictionary['description'] = input("Introduiex una breu descripcio:")
        dictionary['postum'] = input("postum[si/no]:")
        dictionary['decree'] = input("Introdueix el Decret:")
        dictionary['url'] = input("Introdueix la URL:")
        with open('creussj.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['year', 'name', 'pe', 'gender','description','postum','decree','url']
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if capçelera == "si":
                writeCSV.writeheader()  # Se encarrega que de escriure la capçalera del CSV.
                capçelera = "no"
            try:
                writeCSV.writerow(dictionary)
            except:
                print("No s'ha pogut inserir el registre.")
            else:
                print("El registre s'ha inserit correctament.")
        y = y + 1