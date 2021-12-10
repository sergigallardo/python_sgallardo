def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    consonants = [ i for i in state if i not in 'AaEeIiOoUu']
    #Elimina las letras vocales de la frase de la variable state
    print(consonants)

if __name__ == '__main__':
    main()