def main():
    classroom = []
    date = []
    pc = []
    incidence = []
    regist ={
        'aula': classroom,
        'data': date,
        'equip': pc,
        'incidencia': incidence,
    }
    r=1
    s=0
    while r !=0:
        x = str(input("Introduiex la data d'avui:"))
        regist['data'].append(x)
        x = int(input("Introduiex el numero de aula:"))
        regist['aula'].append(x)
        x = str(input("Introduiex el nom del equip:"))
        regist['equip'].append(x)
        x = str(input("Explica la incidencia:"))
        regist['incidencia'].append(x)
        s+=1
        r=int(input("Vols registrar un altre incidencia (Si = 1 / No = 0):"))


    print("Data\t\tAula\t\tEquip\t\tIncidencia")
    for x in range(s):
        print(regist['data'][x],"\t\t",regist['aula'][x],"\t\t",regist['equip'][x],"\t\t",regist['incidencia'][x])





if __name__ == '__main__':
    main()
