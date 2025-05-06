import random
import math
import os
import matplotlib.pyplot as plt
import pandas as pd

def iniciarMenu():
    
    seHaEligidoDistribucion = 0
    limInf = 0
    limSup = 0
    media = 0
    desviacion = 0


    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bienvenido al generador de números aleatorios")
            print("1. Elegir distribución")
            print("2. Generar una lista de números aleatorios")
            print("3. Generar histograma")
            print("4. Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Distribuciones disponibles:")
                print("1. Uniforme")
                print("2. Normal")
                print("3. Exponencial")

                distribucionElegida = int(input("Seleccione una distribución: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                if distribucionElegida == 1:
                    seHaEligidoDistribucion = 1
                    print("Distribución uniforme elegida.")
                    print("Especifique los límites inferior y superior.")
                    limInf = int(input("Límite inferior: "))
                    limSup = int(input("Límite superior: "))
                    print(f"Limites elegidos: {limInf} y {limSup}.")

                elif distribucionElegida == 2:

                    print("Distribución normal elegida.")
                    seHaEligidoDistribucion = 2
                    print("Especifique la media y la desviación estándar.")
                    media = int(input("Media: "))
                    desviacion = int(input("Desviación estándar: "))
                    print(f"Media elegida: {media} y desviación estándar elegida: {desviacion}.")

                elif distribucionElegida == 3:
                    print("Distribución exponencial elegida.")
                    seHaEligidoDistribucion = 3
                    print("Especifique la media.")
                    media = int(input("Media: "))
                    print(f"Media elegida: {media}.")
                else:
                    print("Opción no válida. Intente de nuevo.")

                input("Distribución elegida. Presione Enter para continuar...")
            elif opcion == 2:
                input("Generar números aleatorios. Presione Enter para continuar...")
                if seHaEligidoDistribucion == 0:
                    print("Primero debe elegir una distribución.")
                    continue

                cantidad = int(input("¿Cuántos números aleatorios desea generar? (Hasta 1 millon de números)"))
                if cantidad <= 0:
                    print("La cantidad debe ser un número positivo.")
                    continue
                if cantidad > 1000000:
                    print("Se ha excedido del limite de 1 millón de números aleatorios.")
                    continue
                if seHaEligidoDistribucion == 1 and (limInf >= limSup):
                    print("El límite inferior debe ser menor que el límite superior.")
                    continue

                if seHaEligidoDistribucion == 1:
                    uniforme(limInf, limSup, cantidad)
                elif seHaEligidoDistribucion == 2:
                    normal(media, desviacion, cantidad)
                elif seHaEligidoDistribucion == 3:
                    exponencial(media, cantidad)

                input("Números generados. Presione Enter para continuar...")

            elif opcion == 3:
                if seHaEligidoDistribucion == 0:
                    print("Primero debe elegir una distribución.")
                    input("Presione Enter para continuar...")
                    continue

                cantidad = int(input("¿Cuántos números aleatorios desea generar? (Hasta 1 millón): "))
                if cantidad <= 0 or cantidad > 1000000:
                    print("Cantidad no válida.")
                    continue

                print("Seleccione cantidad de intervalos del histograma (10, 15, 20 o 25):")
                intervalos = int(input("Cantidad de intervalos: "))
                if intervalos not in [10, 15, 20, 25]:
                    print("Cantidad de intervalos no válida.")
                    continue

                if seHaEligidoDistribucion == 1 and (limInf >= limSup):
                    print("El límite inferior debe ser menor que el superior.")
                    continue

                if seHaEligidoDistribucion == 1:
                    datos = generar_uniforme(limInf, limSup, cantidad)
                elif seHaEligidoDistribucion == 2:
                    datos = generar_normal(media, desviacion, cantidad)
                elif seHaEligidoDistribucion == 3:
                    datos = generar_exponencial(media, cantidad)

                generar_histograma(datos, intervalos)
                input("Presione Enter para continuar...")

            elif opcion == 4:
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")



def uniforme(limInf, limSup, cantidad):
    for i in range(cantidad):
        numeroAleatorio = round((round(random.random(), 4) * (limSup - limInf)) + limInf, 4)
        print(numeroAleatorio, end=", ")

def normal(media, desviacion, cantidad):
    i = 0
    while i < cantidad:
        U1 = round(random.random(), 4)
        U2 = round(random.random(), 4)

        Z0 = math.sqrt(-2 * math.log(U1)) * math.cos(2 * math.pi * U2)
        Z1 = math.sqrt(-2 * math.log(U1)) * math.sin(2 * math.pi * U2)

        # Genera Z0
        print((Z0 * desviacion) + media, end=", ")
        i += 1

        # Genera Z1 solo si falta otro número
        if i < cantidad:
            print((Z1 * desviacion) + media, end=", ")
            i += 1

def exponencial(media, cantidad):
    for i in range(cantidad):
        numeroAleatorio = round((-media)*math.log(1-round(random.random(), 4)), 4)

        print(numeroAleatorio, end=", ")

def generar_uniforme(limInf, limSup, cantidad):
    lista = [round(random.random() * (limSup - limInf) + limInf, 4) for _ in range(cantidad)]
    return lista

def generar_normal(media, desviacion, cantidad):
    lista = []
    i = 0
    while i < cantidad:
        U1 = random.random()
        U2 = random.random()
        Z0 = math.sqrt(-2 * math.log(U1)) * math.cos(2 * math.pi * U2)
        Z1 = math.sqrt(-2 * math.log(U1)) * math.sin(2 * math.pi * U2)
        lista.append(round(Z0 * desviacion + media, 4))
        i += 1
        if i < cantidad:
            lista.append(round(Z1 * desviacion + media, 4))
            i += 1
    return lista

def generar_exponencial(media, cantidad):
    lista = [round(-media * math.log(1 - random.random()), 4) for _ in range(cantidad)]
    return lista

def generar_histograma(datos, intervalos):
    # Tabla de frecuencias con pandas
    conteo, bins = pd.cut(datos, bins=intervalos, retbins=True)
    tabla = pd.value_counts(conteo, sort=False)

    # Mostrar tabla
    print("\nTabla de frecuencias:")
    for intervalo, frecuencia in zip(tabla.index, tabla.values):
        print(f"{intervalo}: {frecuencia}")

    # Dibujar histograma
    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=intervalos, edgecolor='black')
    plt.title(f"Histograma con {intervalos} intervalos")
    plt.xlabel("Intervalos")
    plt.ylabel("Frecuencia")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

