slownik = {"i": "oraz",
           "oraz": "i",
           "nigdy": "prawie nigdy",
           "dlaczego": "czemu"}

path = r"C:\Users\admin\Desktop\tekst\plik.txt"
a = []

with open(path, 'r') as f:
    for line in f:
        for word in line.split():
            try:
                a.append(slownik[word])
            except(KeyError):
                a.append(word)
print(a)
