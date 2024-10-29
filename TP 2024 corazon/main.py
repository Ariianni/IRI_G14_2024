import estados as es
import os

def menuprincipal():
  print("--------------------ELECTOCARDIOGRAMA---------------------------")
  print("1) graficas determinadas")
  print("2) determinar estado")
  print("3) exit")
  op=int(input("¿Que deseas ver?: "))
  if(op==1):
    return 1
  if(op==2):
    return 2
  if(op==3):
    return 3  




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
       if(a==1):
         es.menu()





