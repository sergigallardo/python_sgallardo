def writefile(filename):
    f = open(filename, "a+")
    text = input("Introdueix un text: ")[:100]
    f.write(text)
    print(text)
    f.close()