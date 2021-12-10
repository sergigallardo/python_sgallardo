def main():
    x = 0
    llista = []
    nums = [x for x in range(1000)]
    for m in range(len(nums)):
        x = str(m)
        if x in '6666':
            llista.append(x)

    print(llista)
if __name__ == '__main__':
    main()