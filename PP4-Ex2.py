def main():
    num = []
    y=-1
    for x in range(1000):
        if x%2 == 0:
            num.append(x)
        elif x%3!=0:
            num.append(x)
        else:
            num.append(y)
    print(num)

if __name__ == '__main__':
      main()