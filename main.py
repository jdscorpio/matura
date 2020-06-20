'''
    Zadanie 4 z matury poziom rozszerzony - nowa matura, czerwiec 2020
    Autor: Jarosław Drzeżdżon
    Data: 19 czerwca 2020 r.
'''
from zadanie1 import *

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
    zadanie4_1("przyklad.txt","odp.txt")

if __name__ == "__main__":
    main()
