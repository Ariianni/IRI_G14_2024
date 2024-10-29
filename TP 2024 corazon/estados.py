import os

def menu():
    a=0
    while(a!=9):
        a=0
        print("-----------------¿EN QUE ESTADO QUIERES VER A LA PERSONA?---------------------\n")
        print("se simularan un electrocardiograma con los valores del volumen ventricular y la presion aortica en diferentes situaciones y se graficaran dependiendo de su opción")
        print("1) caminando")
        print("2) durmiendo")
        print("3) corriendo")
        print("9) exit")
        a=int(input("¿En que situacion lo quieres ver ahora?: "))

        match a:
            case 1:
                os.system('cls')
                caminando()
            case 2:
                os.system('cls')
                durmiendo()
            case 3: 
                os.system('cls')
                corriendo()


def caminando():
    print("caminando")

def durmiendo():
    print("durmiendo")

def corriendo():
    print("corriendo")