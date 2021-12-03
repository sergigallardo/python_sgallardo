def main():
    x = 1
    y = 0
    code = []
    phone = []
    age = []
    contact = []  # es definira en el format "SI/NO"
    while x !=0:
        name = str(input("Introdueix el teu nom:"))
        surname1 = str(input("Introdueix el teu primer cognom:"))
        surname2 = str(input("Intrdueix el teu segon cognom:"))
        x = (name[:2] + surname1[:2] + surname2[:2])
        code.append(x)
        x = int(input("Introdueix el numero de telefon:"))
        phone.append(x)
        x = int(input("Introdueix la teva edat:"))
        age.append(x)
        x = int(input("Es pot contactar: 1. SI / 2.NO"))
        match x:
            case 1:
                x = "SI"
            case 2:
                x = "NO"
        contact.append(x)
        y+=1
        x = int(input("Vols introduir un altre registre: 1. Si / 0.No"))

    print("Codi\t\tTelefon\t\tEdat\t\tContacte")
    for x in range(y):
        print(code[x],"\t\t",phone[x],"\t\t",age[x],"\t\t",contact[x])

if __name__ == '__main__':
    main()