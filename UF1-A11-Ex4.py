def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    espai  = [i for i in state  if i in ' ']
    print(len(espai), end=" ") # Cuenta los espacios que tiene la frase de la variable state.
    print("espacios")
if __name__ == '__main__':
    main()