import json
temp = '0'
while temp != '2':
    with open('kino.txt') as f:
        data = json.load(f)
    print(data)
    temp = input("Dzialanie: 0 - dodaj, 1 - usuń, 2 - wyjdz: ")

    if temp == '0':

        title = input('Tytul ')
        description = input('Fabula ')
        data["filmy"].append({"tytul":title, "fabula": description})

        with open('kino.txt', 'w') as json_file:

            json.dump(data, json_file)

    elif temp == '1':

        title = input("Podaj tytuł do usunięcia: ")

        for i in range(len(data)):
            if data["filmy"][i]['tytul'] == title:
                del data["filmy"][i]
                with open('kino.txt', 'w') as json_file:
                    json.dump(data, json_file)
                break