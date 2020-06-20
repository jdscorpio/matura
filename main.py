'''
    Zadanie 4 z matury poziom rozszerzony - nowa matura, czerwiec 2020
    Autor: Jarosław Drzeżdżon
    Data: 19 czerwca 2020 r.
'''
from zadanie1 import *
from zadanie2 import *

def zadanie4_1(filename_in:str,filename_ou:str):
    output = open(filename_ou,"w")
    output.write("4.1:\n")   

    with open(filename_in) as file:
        for line in file:
            n,txt = line.split()
            temp = goldbach(int(n))
            if temp[0]!=0:
                output.write(f"{n} {temp[0]} {temp[1]}\n") 
    

def main():
    filein = "przyklad.txt"
    fileout = "odp.txt"
    zadanie4_1(filein, fileout)

    filein = "pary.txt"
    fileout = "wynik4.txt"
    zadanie4_1(filein, fileout)

if __name__ == "__main__":
    main()
