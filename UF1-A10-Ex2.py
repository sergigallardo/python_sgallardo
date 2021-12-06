def main():
    suspesos = []
    aprobats = []
    x = 1
    a = 0
    s = 0
    ms = 0
    ma = 0
    while x != 0:
        nota = int(input("Introdueix una nota:"))

        if nota >= 5:
            aprobats.append(nota)
            ma = nota + ma
            a += 1
        else:
            suspesos.append(nota)
            ms = nota + ms
            s += 1
        x = int(input("Vols introduir una altre nota: 1. Si / 0. No"))
    ma = ma / a
    ms = ms / s
    print("Aprobats:", end=" ")
    for x in range(a):
        print(aprobats[x], end=" ")
    x = 0
    print("Mitjana Aprobats:", end=" ")
    print(ma)
    print("Suspesos:", end=" ")
    for x in range(s):
        print(suspesos[x], end=" ")
    print("Mitjana suspesos:", end=" ")
    print(ms)


if __name__ == '__main__':
    main()
