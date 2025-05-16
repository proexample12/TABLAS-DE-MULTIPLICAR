"""
Autor: Kenneth M Zamora H 
fecha: 16/5/2025
version: 1.0
Descripcion: 

"""

import os 

def multiplicar():
    os.system("cls")
    print("****************TABLAS DE MULTIPLICAR****************")
    n=int(input("ingrese LA TABLA DE MULTIPLICAR INICAL: "))
    m=int(input("INGRESE LA TABLA DE MULTIPLICAR FINAL: "))
    print("-------------------------------------------------------")
    print(f"//////////Tabla de multiplicar de 1 hasta {m}////////////////")
    print("-------------------------------------------------------")
    for i in range(1,n+1,1):   
        for j in range(1,m+1,1):
            print(f"{i} x {j} = {i*j}")
            print("\n")
        print("-------------------------------------------------------")

multiplicar()
