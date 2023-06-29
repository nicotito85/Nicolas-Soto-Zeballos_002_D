import numpy
import random as rn
from Atencion import *
arreglo=numpy.array([])



def grabar(arreglo):
    a=Atencion()
    c = False
    while c==False:
        c=a.setCodigoAtencion(input("ingrese codigo"))
    c=False
    while c==False:
        c=a.setNombreCliente(input("ingrese nombre cliente"))

    a.fechaAtencion=input("ingrese fecha atencion")
    a.horaAtencion=input("ingrese hora atencion")
    a.DescripcionAtencion=input("ingrese descripcion atencion")
    c=False
    while c==False:
        c=a.setPrecioAtencion=int(input("ingrese valor Atencion"))
    return numpy.append(arreglo,a)


def buscar(arreglo):
    print("buscar cita")
    codigo = input("ingrese su codigo de atencion")
    for Atencion in arreglo:
        if Atencion.CodigoAtencion == codigo:
            print(f"{Atencion.CodigoAtencion}")
            print(f"{Atencion.NombreCliente}")
            print(f"{Atencion.FechaAtencion}")
            print(f"{Atencion.horaAtencion}")
            print(f"{Atencion.DescripcionAtencion}")
            print(f"{Atencion.PrecioAtencion}")
        else:
            print("numero de cita no encontrado")


def imprimir(arreglo):
    print("buscar cita")
    codigo = input("ingrese su codigo de atencion")
    for Atencion in arreglo:
            if Atencion.CodigoAtencion == codigo:
                print(f"{Atencion.CodigoAtencion}")
                print(f"{Atencion.NombreCliente}")
                print(f"{Atencion.FechaAtencion}")
                print(f"{Atencion.horaAtencion}")
                print(f"{Atencion.DescripcionAtencion}")
                print(f"{Atencion.PrecioAtencion}")
                print(f"numero de atencion \t{rn.randint(1000,9999,)}")
                print(f"propina de \t{rn.randint(100,1000)}")
            else:
                print("numero de cita no encontrado")



def salir(arreglo):
    ciclo=False
ciclo=True
while ciclo:
    print("Peluqueria Mechas locas")
    print("ingreso de datos")
    print("1)ingreso Atencion")
    print("2)revicion Atencion")
    print("3)Impresion Atencion")
    print("4)salir")
    try:

        op=int(input("porfavor escoja una opcion"))
        match op:
            case 1:
                arreglo=grabar(arreglo)


            case 2:
                arreglo=buscar(arreglo)

            case 3:
                arreglo=imprimir(arreglo)

            case 4:
                ciclo=False
                print("Nicolas Soto")
                print("version 0.7.5")
            case _:
                print("porfavor ingrese una opcion valida")

    except BaseException as error:
        print(f"{error}")