class Zespolone():
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def dodawanie(self, liczba1):
        return self.re + liczba1[0], self.im + liczba1[1]

    def odejmowanie(self, liczba1):
        return self.re - liczba1[0], self.im - liczba1[1]

    def mnozenie(self, liczba):
        return self.re*liczba[0] - self.im * liczba[1], self.im * liczba[0] + self.re * liczba[1]

    def getter(self):
        return self.re, self.im

    def setter(self, liczba1):
        self.re = liczba1[0]
        self.im = liczba1[1]

    def __str__(self):
        return "({0},{1})".format(self.re, self.im)

    def __add__(self, other):
        x = self.re + other.re
        y = self.im + other.im
        return Zespolone(x, y)

    def __sub__(self, other):
        x = self.re - other.re
        y = self.im - other.im
        return Zespolone(x, y)

liczba = Zespolone(1, 2)
liczba2 = Zespolone(3,4)

print(liczba.dodawanie((3, 4)))
print(liczba + liczba2)

