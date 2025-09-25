from concesionario import Concesionario
from automovil_constructor import AutomovilConstructor

if __name__ == "__main__":
    print("----> Creamos el constructor (builder)")
    constructor = AutomovilConstructor()

    print("----> Creamos el concesionario (director)")
    concesionario = Concesionario()

    print("----> Creamos un SUV (construirSUV)")
    suv = concesionario.construirSUV(constructor)
    print("SUV: ", suv)
    try:
        suv.color = "Error"
        print("Mutable")
    except:
        print("Inmutable")


    print("----> Creamos un deportivo (construirDeportivo)")
    deportivo = concesionario.construirDeportivo(constructor)
    print("Deportivo: ", deportivo)
    try:
        deportivo.color = "Error"
        print("Mutable")
    except:
        print("Inmutable")


    print("----> Creamos un basico (construirBasico)")
    basico = concesionario.construirBasico(constructor)
    print("Basico: ", basico)
    try:
        basico.color = "Error"
        print("Mutable")
    except:
        print("Inmutable")
    