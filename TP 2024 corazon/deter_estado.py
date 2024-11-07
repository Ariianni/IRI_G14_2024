import estados as es
def deter_estados():
    
    diastolica = int(input("Introduzca su presión diastólica"))
    sistolica = int(input("Introduzca su presión sistólica"))

    if 130 <= sistolica <= 150 and diastolica >= 70 and diastolica <= 80:
        print("Estado: Caminando")
        es.caminando()
    elif 160 <= sistolica <= 200 and 70 <= diastolica <= 90:
        print("Estado: Corriendo")
        es.corriendo()
    elif 90 <= sistolica <= 120 and 60 <= diastolica <= 80:
        print("Estado: Durmiendo")
        es.durmiendo()

