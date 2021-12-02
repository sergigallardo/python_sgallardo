#Aquest codi valida el numero introduit per teclat si es Natural o no.
def main():
    num = int(input("Introdueix un valor numeric:"))
    while num<=0:
        num = int(input("Error! Introdueix un valor valid:"))

if __name__ == '__main__':
    main()


