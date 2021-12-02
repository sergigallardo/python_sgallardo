def main():
    y = 0
    registers=int(input("Introdueix el numero de registres que vols introduir:"))
    while y < registers:
        codi = []
        phone = []
        age = []
        contact = [] # es definira en el format "SI/NO"
        name = str(input("Introdueix el teu nom:"))
        surname1 = str(input("Introdueix el teu primer cognom:"))
        surname2 = str(input("Intrdueix el teu segon cognom:"))
        x = (name[:2] + surname1[:2] + surname2[:2])
        codi.append(x)
        x = int(input("Introdueix el numero de telefon"))
        phone.append(x)
        x = int("Introdueix la teva edat:")
        age.append(x)
        x = int(input("Es pot contactar: 1. SI / 2.NO"))
        match x:
            case 1:
                x = "SI"
            case 2:
                x = "NO"
        contact.append(x)

if __name__ == '__main__':
    main()