import os
import numpy as np
import matplotlib.pyplot as plt

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
    T = 120
    tiempo = np.linspace(
        0, T, 1000
    )
    #---------Mascaras de volumen ventricular----------------
    mask1 = (tiempo <= (10))#0.347 + 1.5
    mask2 = ((tiempo > (10)) & (tiempo <= (50)))
    mask3 = ((tiempo > (50)) & (tiempo <= (90)))
    mask4 = ((tiempo > (90)) & (tiempo <= (110)))
    mask5 = ((tiempo > (110)) & (tiempo <= (120)))

    #--------Mascaras de presion aortica-------------------
    Amask1 = (tiempo <= (21.5))
    Amask2 = ((tiempo > (21.5)) & (tiempo <= (40)))
    Amask3 = ((tiempo > (40)) & (tiempo <= (43.2)))
    Amask4 = ((tiempo > (43.2)) & (tiempo <= (120)))

    #-------------Volumen ventricular---------------------------
    yV = np.zeros_like(tiempo)  # Crear un array de ceros del mismo tamaño que tiempo
    yV = yV + mask1 * ((1 / 50000) * np.exp(tiempo - 0.03) + 100)
    yV = yV + mask2 * ((-np.log10((tiempo-9)**20))+80)
    yV = yV + mask3 * ((1*np.log10((tiempo -48)**20)+50))
    yV = yV + mask4 * (13*np.sin(((1/10) * (tiempo))+3)+89)
    yV = yV + mask5 * (-np.sin(((1 / 4) * (tiempo)-3))+ 101)
    yV_total = np.tile(yV, 3)
    tiempo_V_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 1)
    plt.xlabel("  sistole  diastole        sistole  diastole         sistole  diastole",loc='left')
    plt.ylabel("Volumen(ml)")
    plt.grid()
    plt.plot(tiempo_V_total, yV_total)

    #--------------presion aortica-------------------------
    yA = np.zeros_like(tiempo)  # Crear un array de ceros del mismo tamaño que tiempo
    yA = yA + Amask1*(80)
    yA = yA + Amask2*(-40*np.sin(0.135*tiempo+0.3)+80)
    yA = yA + Amask3*((tiempo-41.35)**(2)+100)
    yA = yA + Amask4*(np.exp(-0.07*tiempo+6.16)+80)
    yA_total = np.tile(yA, 3)
    tiempo_A_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 2)
    plt.xlabel("  sistole  diastole        sistole  diastole         sistole  diastole",loc='left')
    plt.ylabel("Presión(mmHg)")
    plt.plot(tiempo_A_total, yA_total)
    plt.grid()


    plt.show()


def durmiendo():
    print("durmiendo")

def corriendo():
    print("corriendo")