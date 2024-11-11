import estados as es
import deter_estado as dt
import os
import matplotlib as ma
import numpy as np
def menuprincipal(): 
  print("--------------------ELECTOCARDIOGRAMA---------------------------")
  print("1) graficas determinadas")
  print("2) determinar estado")
  print("3) exit")
  op=0
  while(op!=1 and op!=2):
    op=int(input("¿Que deseas ver?: "))
    if(op == 1):
      return 1
    if(op == 2):
      return 2
    if(op == 3):
      return 3  
    if(op!=1 and op!=2):
      print("error, no se encuentra en las opciones")




a=0
while(a!=3):
    a=0
    a=menuprincipal()
    os.system('cls')
    match a:
      case 1:
       print("condiciones fisicas: ")
       print("1) normales")
       a=int(input("ingrese tu condicion fisica: "))
       if(a == 1):
         es.menu()
      case 2:
        print("determinar estado: ")
        if(a == 2):
          dt.deter_estados()





