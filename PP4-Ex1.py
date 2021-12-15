def main():
    y = 0
    c = 0
    numeros = []
    for x in range(26):
        if x % 2 == 0:
            y = x*3
            numeros.append(y)
        else:
            y = int(x/2)
            numeros.append(y)
        c+=1
    c= c - 7
    for x in range(c):
        print(numeros[x], end=" ")
if __name__ == '__main__':
      main()