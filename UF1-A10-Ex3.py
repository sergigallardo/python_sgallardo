def main():
   insti = {
       "user":[],
       "depart":[],
       "classroom":[]
   }
   x = 1
   while x != 0:
       x = str(input("Introdueix el nom de usuari:"))
       insti["user"].append(x)
       x = str(input("Introdueix el nom del departament:"))
       insti["depart"].append(x)
       x = 0
       while 15 < x or x<1:
           x = int(input("Introdueix el numero de l'Aula:"))
       insti["classroom"].append(x)
       x = int(input("Vols introduir un altre usuari: 1.Si / 0. No:"))
   print("Usuaris:", end=" ")
   print(insti["user"])
   print("Departaments:",end=" ")
   print(insti["depart"])
   print("Classe:", end=" ")
   print(insti["classroom"])
if __name__ == '__main__':
    main()