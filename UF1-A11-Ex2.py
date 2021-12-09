def main():
    x = 0
    llista = [x  for x in range(1000) if x % 8 == 0]
    print(llista)
if __name__ == '__main__':
    main()