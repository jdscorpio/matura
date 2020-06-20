'''
    Zadanie 4 z matury poziom rozszerzony - nowa matura, czerwiec 2020
    Autor: Jarosław Drzeżdżon
    Data: 19 czerwca 2020 r.
'''
from zadanie1 import *
from zadanie2 import *
from zadanie3 import *

def zadanie4_1(filename_in:str,filename_out:str):
    output = open(filename_out,"w")
    output.write("4.1:\n")   

    with open(filename_in) as file:
        for line in file:
            n,txt = line.split()
            temp = goldbach(int(n))
            if temp[0]!=0:
                output.write(f"{n} {temp[0]} {temp[1]}\n") 
    
def zadanie4_2(filename_in:str,filename_out:str):
    output = open(filename_out,"a")
    output.write("\n4.2:\n")
    with open(filename_in) as file:
        for line in file:
            n,txt = line.split()
            temp = LCF(txt)
            output.write(f"{temp[0]} {temp[1]}\n")

def zadanie4_3(filename_in:str,filename_out:str):
    output = open(filename_out,"a")
    output.write("\n4.3:\n")
    tab = []
    with open(filename_in) as file:
        for line in file:
            n,txt = line.split()
            if numEqualWord(int(n),txt):
                tab.append(n + ' ' + txt)
    for i in range(len(tab)):
        n1,txt1 = tab[i].split()
        for j in range(i+1,len(tab)):
            n2,txt2 = tab[j].split()
            nn,txtt = por(int(n1),txt1, int(n2),txt2)
    output.write(f"{len(txtt)} {txtt}")

def main():
    filein = "przyklad.txt"
    fileout = "odp.txt"
    zadanie4_1(filein, fileout)
    zadanie4_2(filein, fileout)
    zadanie4_3(filein, fileout)

    filein = "pary.txt"
    fileout = "wynik4.txt"
    zadanie4_1(filein, fileout)
    zadanie4_2(filein, fileout)
    zadanie4_3(filein, fileout)

if __name__ == "__main__":
    main()
