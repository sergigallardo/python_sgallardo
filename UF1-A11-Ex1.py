def main():
    x = 0
    llista = [x + 1 for x in range(30) if x % 2 != 0]
    print(llista)
if __name__ == '__main__':
    main()