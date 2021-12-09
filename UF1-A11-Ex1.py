def main():
    x = 0
    parells = [x + 1 for x in range(30) if x % 2 != 0]
    print(parells)
if __name__ == '__main__':
    main()