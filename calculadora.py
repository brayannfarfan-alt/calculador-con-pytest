from calculadora.utils import pedir_numero, pedir_opcion
from calculadora.operaciones import sumar, restar , multiplicar, dividir

while True:
    opcion = pedir_opcion()

    a = pedir_numero("Ingresa primer numero")
    b = pedir_numero("Ingresa segundo numero")

    match opcion:
        case "1":
            print("Resultado ", sumar(a,b) )
        case "2":
            print("Resultado ", restar(a,b))
        case "3":
            print("Resultado ", multiplicar(a,b) )
        case "4":
            print("Resultado ", dividir(a,b))
            
    otra = input("¿Querés hacer otra operacion ( s/n )")

    if otra != "s":
        print("Hasta la proxima!!!!!")
        break