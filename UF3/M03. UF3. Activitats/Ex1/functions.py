
def writefile(filename):
    f = open(filename, "w") #Obre el arxiu text.txt y si no existeix el crea.
    text = input("Introdueix un text: ")[:100] #[:100] el posem per limitar el numero de caracters a escriure.
    #En el cas que ens pasem del numero de caractes sol agafara els 100 caractes.
    f.write(text) #Escriu en el document text.txt.
    print(text) #Printa per pantalla tot el que hem introduit en el input.
    f.close()