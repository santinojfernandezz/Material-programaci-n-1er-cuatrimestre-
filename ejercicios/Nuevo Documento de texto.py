#Ejercicios Funciones
def par_impar (num_ingresado):
    if (num_ingresado % 2) == 0: 
        print("el numero es par")
    else: 
        print("el numero es impar")

numero = input("Ingrese un numero para saber si es impar o par: ")
numero = int(numero)

par_impar(numero)
