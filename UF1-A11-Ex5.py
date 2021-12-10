def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    consonants = [ i for i in state if i not in 'AaEeIiOoUu']
    print(consonants)

if __name__ == '__main__':
    main()