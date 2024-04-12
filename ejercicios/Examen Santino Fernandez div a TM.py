import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:santino
apellido:fernandez
Div : A
dni : 47 057 398
---
Examen:
---
Enunciado:
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el tipo mas ingresado (gato ,perro o exotico) ###
Informe B- El porcentaje de mascotas femeninas y el de las masculinas. ###
Informe C -El tipo de la mascota más pesada ###
Informe D- El nombre del gato más joven ###
Informe E- El promedio de peso de todas las mascotas
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_gatos = 0
        contador_perros = 0
        contador_exotico = 0
        contador_masc = 0
        contador_fem = 0
        gato_mas_joven = "no se ingreso ningun gato"
        bandera_mas_pesada = 0
        peso_general = 0

        for i in range (5):
            nombre = prompt("Info", "Ingrese su nombre")
            edad = prompt("Info", "Ingrese la edad de su mascota")
            edad = int(edad)
            while edad < 1 :
                edad = prompt("Info", "Reigrese la edad de su mascota")
                edad = int(edad)

            tipo = prompt("Info", "Ingrese el tipo de mascota(gato ,perro o exotico)")
            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt("Info", "reingrese el tipo de mascota(gato ,perro o exotico)")

            sexo = prompt("Info", "Ingrese el sexo de su mascota (f o m)")
            while sexo != "f" and sexo != "m" :
                sexo = prompt("Info", "reigrese el sexo de su mascota (f o m)")

            peso = prompt("info", "ingrese el peso de su mascota")
            peso = int(peso)
            while peso < 10 or peso > 80:
                peso = prompt("info", "reingrese el peso de su mascota")
                peso = int(peso)
            
            match tipo :
                case "gato":
                    if contador_gatos == 0 :
                        gato_mas_joven = nombre
                        edad_gato_mas_joven = edad
                    else :
                        if edad_gato_mas_joven > edad :
                            gato_mas_joven = nombre
                            edad_gato_mas_joven = edad
                    contador_gatos = contador_gatos + 1
                case "perro":
                    contador_perros = contador_perros + 1
                case _:
                    contador_exotico = contador_exotico + 1
            
            if bandera_mas_pesada == 0:
                bandera_mas_pesada += 1
                mascota_mas_pesada = peso
                tipo_mas_pesado = tipo
            else :
                if mascota_mas_pesada < peso:
                    mascota_mas_pesada = peso
                    tipo_mas_pesado = tipo
            if sexo == "f":
                contador_fem = contador_fem + 1
            else: 
                contador_masc = contador_masc + 1

            peso_general = peso_general + peso
        
        porcentaje_fem = (contador_fem * 100) / 5
        porcentaje_masc = (contador_masc * 100) / 5

        promedio_peso_gral = peso_general / 5

        if contador_gatos > contador_exotico and contador_gatos > contador_perros :
            tipo_mas_ingresado = "gato"
        elif contador_perros > contador_exotico :
            tipo_mas_ingresado = "perro"
        else:
            tipo_mas_ingresado = "exotico"

        mensaje = f"HUbo un {porcentaje_fem}% de mascotas femeneninas y un {porcentaje_masc}% de mascotas masculinas. El tipo de mascota mas ingresado fue {tipo_mas_ingresado}, el tipo de mascota mas pesado fue {tipo_mas_pesado} y en promedio todas las mascotas ingresadas tienen un peso de {promedio_peso_gral}kg. El nombre del gato mas joven es {gato_mas_joven}. "

        print(mensaje)
        

            
       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()