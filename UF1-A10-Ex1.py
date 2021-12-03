def main():
    n1 = int(input("Introdueix un valor numeric per a n1:"))
    n2 = int(input("Introdueix un valor numeric per a n2:"))

    if n1 < n2:
        print("Interval:",end=" ")
        while n1 < n2:
            n1+=1
            if n1 != n2:
                print(n1, end=" ")
    else:
        print("Error! n1 < n2 no es correcte n1 es major que n2.")
if __name__ == '__main__':
    main()
