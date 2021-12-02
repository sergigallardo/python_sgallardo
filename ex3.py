def main():
    sum=0
    count = 0
    num = int(input("Introdueix un valor numeric:"))
    print("Seqüencia:",end=" ")
    while sum+count<=num:
        count = count + 1
        print(count,end=" ")
        if sum+count<=num:
            sum=sum+count

    print("Suma Total:", end=" ")
    print(sum)
if __name__ == '__main__':
    main()