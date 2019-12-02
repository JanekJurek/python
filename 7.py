path = r"C:\Users\admin\Desktop\tekst\plik.txt"
a=[]
with open(path, 'r') as f:
    for line in f:
        for word in line.split():
            if word != 'sie' and  word != 'i':
                a.append(word)
print(a)


