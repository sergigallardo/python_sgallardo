def main():
    llista = list()
    x = 0
    x = int(input("Introdueix un valor numeric:"))
    while x != 0:
        llista.append(x)
        x = int(input("Introdueix un valor numeric:"))

    print(llista)


if __name__ == '__main__':
    main()
