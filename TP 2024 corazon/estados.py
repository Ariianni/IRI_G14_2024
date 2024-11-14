import os
import numpy as np
import matplotlib.pyplot as plt
import random as rd

T = 120
tiempo = np.linspace(
    0, T, 1000
)
#---------Mascaras de volumen ventricular----------------
mask1 = (tiempo <= (10))
mask2 = ((tiempo > (10)) & (tiempo <= (50)))
mask3 = ((tiempo > (50)) & (tiempo <= (90)))
mask4 = ((tiempo > (90)) & (tiempo <= (110)))
mask5 = ((tiempo > (110)) & (tiempo <= (120)))

#--------Mascaras de presion aortica-------------------
Pmask1 = (tiempo >= 0) & (tiempo <= 1.99)
Pmask2 = (tiempo > 1.99) & (tiempo <= 27)
Pmask3 = (tiempo > 27) & (tiempo <= 44.5)
Pmask4 = (tiempo > 44.5) & (tiempo <= 120)

def menu():
    a=0
    while(a!=9):
        a=0
        print("-----------------¿EN QUE ESTADO QUIERES VER A LA PERSONA?---------------------\n")
        print("se simularan un electrocardiograma con los valores del volumen ventricular y la presion aortica en diferentes situaciones y se graficaran dependiendo de su opción")
        print("1) caminando")
        print("2) durmiendo")
        print("3) corriendo")
        print("4) arritmia")
        print("5) fibrilacion ventricular")
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
            case 4:
                os.system('cls')
                arritmia()
            case 5:
                os.system('cls')
                fibrilacion()

def caminando():
    print("caminando")

    #-------------Volumen ventricular---------------------------
    VD=150
    VS=80
    yV = np.zeros_like(tiempo)  # Crear un array de ceros del mismo tamaño que tiempo
    yV = yV + mask1 * (VD)#(1 / 50000) * np.exp(tiempo - 0.03) +
    yV = yV + mask2 * (((VD*(np.exp(-tiempo+2.3))**(1/(10)))+VS))
    yV = yV + mask3 * ((1*np.log10((tiempo -48)**20)+VS-5))
    a=(1*np.log10((tiempo -48)**20)+VS-5)
    yV = yV + mask4 * ((VD-a-6)*np.sin(((1/10) * (tiempo))+3.4)+a+6)
    yV = yV + mask5 * (-np.sin(((1 / 4) * (tiempo)-3))+VD)

    yV_total = np.tile(yV, 3)
    tiempo_V_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 1)
    #plt.xlabel("  sistole  diastole        sistole  diastole         sistole  diastole",loc='left')
    plt.ylabel("Volumen(ml)")
    plt.grid()
    plt.plot(tiempo_V_total, yV_total)

    #--------------presion aortica-------------------------
    Ps = 120  
    Pd = 80  
    yP = np.zeros_like(tiempo)
    yP += Pmask1 * (-((Ps - Pd) / 20) * np.sin(0.15 * tiempo) + Pd)
    yP += Pmask2 * (-((1) / 8) * (tiempo - ((Ps - Pd) / 2))**2 + Ps)
    yP += Pmask3 * ((1 / 11) * (tiempo - (Ps - Pd))**2 + Pd +19)
    yP += Pmask4 * (np.exp(-0.189 * tiempo + 10) + Pd)
    yA_total = np.tile(yP, 3)
    tiempo_A_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 2)
    #plt.xlabel("  sistole  diastole        sistole  diastole         sistole  diastole",loc='left')
    plt.ylabel("Presión(mmHg)")
    plt.plot(tiempo_A_total, yA_total)
    plt.grid()


    plt.show()

def durmiendo():
    print("durmiendo")

    #-------------Volumen ventricular---------------------------
    VDd=120
    VSd=80
    y3 = np.zeros_like(tiempo)
    y3 = y3 + mask1 * (VDd)
    y3 = y3 + mask2 * (((VDd*(np.exp(-tiempo-1))**(1/(10)))+VSd))
    y3 = y3 + mask3 * ((1*np.log10((tiempo -48)**20)+VSd-5))
    cesar=(1*np.log10((tiempo -48)**20)+VSd-5)
    y3 = y3 + mask4 * ((VDd-cesar-6)*np.sin(((1/10) * (tiempo))+3.4)+cesar+6)
    y3 = y3 + mask5 * (-np.sin(((1 / 4) * (tiempo)-3))+VDd)

    yV_total = np.tile(y3, 3)
    tiempo_V_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 1)
    plt.ylabel("Volumen(ml)")
    plt.grid()
    plt.plot(tiempo_V_total, yV_total)

    #--------------presion aortica-------------------------
    Ps = 120  
    Pd = 80  
    yP = np.zeros_like(tiempo)
    yP += Pmask1 * (-((Ps - Pd) / 20) * np.sin(0.15 * tiempo) + Pd)
    yP += Pmask2 * (-((1) / 8) * (tiempo - ((Ps - Pd) / 2))**2 + Ps)
    yP += Pmask3 * ((1 / 11) * (tiempo - (Ps - Pd))**2 + Pd +19)
    yP += Pmask4 * (np.exp(-0.189 * tiempo + 10) + Pd)
    yA_total = np.tile(0.75*yP, 3)
    tiempo_A_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 2)
    #plt.xlabel("  sistole  diastole        sistole  diastole         sistole  diastole",loc='left')
    plt.ylabel("Presión(mmHg)")
    plt.plot(tiempo_A_total, yA_total)
    plt.grid()


    plt.show()

def corriendo():
    print("corriendo")
    #-------------Volumen ventricular---------------------------
    VDc=200
    VSc=90
    y2 = np.zeros_like(tiempo)
    y2 = y2 + mask1 * (VDc)
    y2 = y2 + mask2 * (((VDc*(np.exp(-tiempo+4))**(1/(10)))+VSc))
    y2 = y2 + mask3 * ((1*np.log10((tiempo -48)**20)+VSc-5))
    cesar=(1*np.log10((tiempo -48)**20)+VSc-5)
    y2 = y2 + mask4 * ((VDc-cesar-6)*np.sin(((1/10) * (tiempo))+3.4)+cesar+6)
    y2 = y2 + mask5 * (-np.sin(((1 / 4) * (tiempo)-3))+VDc)



    yV_total = np.tile(y2, 3)
    tiempo_V_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 1)
    plt.ylabel("Volumen(ml)")
    plt.grid()
    plt.plot(tiempo_V_total, yV_total)

    #--------------presion aortica-------------------------
    Ps = 120  
    Pd = 80  
    yP = np.zeros_like(tiempo)
    yP += Pmask1 * (-((Ps - Pd) / 20) * np.sin(0.15 * tiempo) + Pd)
    yP += Pmask2 * (-((1) / 8) * (tiempo - ((Ps - Pd) / 2))**2 + Ps)
    yP += Pmask3 * ((1 / 11) * (tiempo - (Ps - Pd))**2 + Pd +19)
    yP += Pmask4 * (np.exp(-0.189 * tiempo + 10) + Pd)
    yA_total = np.tile(1.17*yP, 3)
    tiempo_A_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 2)
    #plt.xlabel("  sistole  diastole        sistole  diastole         sistole  diastole",loc='left')
    plt.ylabel("Presión(mmHg)")
    plt.plot(tiempo_A_total, yA_total)
    plt.grid()


    plt.show()

def arritmia():
    print("arritmia")

    Ps = rd.randint(100, 200)  
    Pd = rd.randint(10, 70)


    # Inicializa yP con ceros
    yA = np.zeros_like(tiempo)
    yA += mask1 * (-((Ps - Pd) / 20) * np.sin(0.15 * tiempo) + Pd)
    yA += mask2 * (-((1) / 8) * (tiempo - ((Ps - Pd) / 2))**2 + Ps)
    yA += mask3 * ((1 / 11) * (tiempo - (Ps - Pd))**2 + Pd +19)
    yA += mask4 * (np.exp(-0.189 * tiempo + 10) + Pd)

    yA_total = np.tile(yA, 3)
    tiempo_A_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 1)
    plt.ylabel("Volumen(ml)")
    plt.grid()
    plt.plot(tiempo_A_total, yA_total)

    plt.show()

def fibrilacion():
    print("fibrilacion")
    #----------------------PRESION AORTICA----------------
    Ps=120
    Pd=80
    #-----------mascaras de aorta------------
    FAmask1 = (tiempo >= 0) & (tiempo <= 1.99)
    FAmask2 = (tiempo > 1.99) & (tiempo <= 27)
    FAmask3 = (tiempo > 27) & (tiempo <= 44.5)
    FAmask4 = (tiempo > 44.5) & (tiempo <= 59.6)
    FAmask5 = (tiempo > 59.6) & (tiempo <= 120)

    # Inicializa yP con ceros
    yP = np.zeros_like(tiempo)

    #-----------------Funcion--------------------------
    yP += FAmask1 * (-((Ps - Pd) / 20) * np.sin(0.15 * tiempo) + Pd)
    yP += FAmask2 * (-((1) / 8) * (tiempo - ((Ps - Pd) / 2))**2 + Ps)
    yP += FAmask3 * ((1 / 11) * (tiempo - (Ps - Pd))**2 + Pd + 19)
    yP_exp = np.exp(-0.189 * tiempo + 10) + Pd
    yP += FAmask4 * yP_exp

    #  punto de transición
    transicion_tiempo = 59.6
    fin_exponencial = np.exp(-0.189 * transicion_tiempo + 10) + Pd
    pendiente_exponencial = -0.189 * np.exp(-0.189 * transicion_tiempo + 10)
    amplitud_seno = 4
    frecuencia_seno = (Ps - Pd) / 30
    fase_inicial = np.arcsin((fin_exponencial - Pd) / amplitud_seno)  # Ajuste para la fase del seno

    yP += FAmask5 * (amplitud_seno * np.sin(frecuencia_seno * (tiempo - transicion_tiempo) + fase_inicial) + Pd)#punto de fibrilacion

    #-----graficar--------
    yA_total = np.tile(yP, 3)
    tiempo_A_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 1)
    plt.ylabel("Presion (mmHg)")
    plt.grid()
    plt.plot(tiempo_A_total, yA_total)

    #----------VOLUMEN VENTRICULAR----------
    #---------Mascaras de volumen ventricular----------------
    FVmask1 = (tiempo <= (10))
    FVmask2 = ((tiempo > (10)) & (tiempo <= (50)))
    FVmask3 = ((tiempo > (50)) & (tiempo <= (59.6)))
    FVmask4 = (tiempo > (59.6))

    VDc=120
    VSc=80
    y2 = np.zeros_like(tiempo)
    y2 = y2 + FVmask1 * (VDc)
    y2 = y2 + FVmask2 * (((VDc*(np.exp(-tiempo-1))**(1/(10)))+VSc))
    y2 = y2 + FVmask3 * ((1*np.log10((tiempo -48)**20)+VSc-5))
    cesar=(1*np.log10((tiempo -48)**20)+VSc-5)
    y2 = y2 + FVmask4 * (amplitud_seno * np.sin(frecuencia_seno * (tiempo - transicion_tiempo) + fase_inicial) + Pd)

    #-----graficar--------
    yV_total = np.tile(y2, 3)
    tiempo_V_total = np.linspace(0, 3 * 120, 3 * len(tiempo))
    plt.subplot(2, 1, 2)
    plt.ylabel("Volumen (ml)")
    plt.grid()
    plt.plot(tiempo_V_total, yV_total)

    plt.show()



