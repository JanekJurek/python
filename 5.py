import os

def wypisuje(path):
    for i in os.listdir(path):
        if os.path.isdir(path + r'\\' + i):
            wypisuje(path + r'\\' + i)
        else:
            print(i)

wypisuje(r'C:\Xilinx\Vivado\2019.1\tps\win64\git-2.16.2')