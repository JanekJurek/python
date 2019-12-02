import random
import threading
from multiprocessing.pool import ThreadPool

def hist(zakres, dane):

    powtorzenia_liczb = [0 for x in range(zakres+1)]

    for i in range(len(dane)):
        powtorzenia_liczb[dane[i]] += 1
    return powtorzenia_liczb



przedzial = 4
ilosc = 12

dane = [random.randint(0, przedzial) for x in range(ilosc)]
dane1 = dane[0:3]
dane2 = dane[3:6]
dane3 = dane[6:9]
dane4 = dane[9:12]

pool = ThreadPool(processes=1)
wynik1 = pool.apply_async(hist, (przedzial, dane1))
wynik2 = pool.apply_async(hist, (przedzial, dane2))
wynik3 = pool.apply_async(hist, (przedzial, dane3))
wynik4= pool.apply_async(hist, (przedzial, dane4))

return_val = wynik1.get()
return_val2 = wynik2.get()
return_val3 = wynik3.get()
return_val4 = wynik4.get()

wynik = [0 for a in range(przedzial+1)]

for i in range(przedzial+1):
    wynik[i] = return_val[i]+return_val2[i]+return_val3[i]+return_val4[i]
