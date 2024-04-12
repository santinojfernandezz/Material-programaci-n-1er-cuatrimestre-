contador_uno = 0
masc_iot_ia = 0
fem_no_ia = 0
bandera_masc = 0
for contador in range (3):
    nombre = input("Ingrese su nombre: ")
    edad = input("ingrese su edad: ")
    edad = int(edad)
    while edad < 18 :
        edad = input("ERROR: ingrese su edad(debe ser mayor de edad): ")
        edad = int(edad)
    genero = input("ingrese su genero(m, f, otro): ")
    while genero != "m" and genero != "f" and genero != "otro":
        genero = input("ERROR: ingrese su genero(m, f, otro): ")
    tecnologia = input("ingrese su tecnologia(IA, RV/RA, IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("ERROR: ingrese su tecnologia(IA, RV/RA, IOT): ")
    match genero :
        case "m":
            if tecnologia == "IA" or tecnologia == "IOT" and edad > 24 and edad < 51:
                masc_iot_ia += 1
            if bandera_masc == 0:
                m_mayor_edad = nombre
                tech_mayor_edad = tecnologia
                mayor_edad = edad
                bandera_masc += 1
            else:
                if edad > mayor_edad:
                    mayor_edad = edad
                    m_mayor_edad = nombre
                    tech_mayor_edad = tecnologia
        case "f":
            if tecnologia == "IA" and edad > 33 and edad < 40:
                fem_no_ia += 1
    contador_uno += 1

total_no_ia = contador_uno - fem_no_ia
porcentaje_no_ia = round((total_no_ia / contador_uno) * 100)

mensaje = f"La cantidad de empleados de género masculino que votaron por IOT o IA de edad entre 25 y 50 años inclusive es de {masc_iot_ia}. Porcentaje de empleados que no votaron por IA, de genero NO Femenino o edad entre los 33 y 40 es de {porcentaje_no_ia}%. Y el empleado masculino de mayor edad({mayor_edad} años)  se llama {m_mayor_edad} y voto la tecnologia {tech_mayor_edad}."
print(mensaje)


