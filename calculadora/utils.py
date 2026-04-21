def pedir_opcion():
    while True:
        print("\n==========CALCULADORA===========")
        print("\nOpciones: ")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")

        opcion = input("Eliga la opcion ( 1-4 )\n")

        opcion_valida = {
            "1":"Sumar",
            "2":"Restar",
            "3":"Multiplicar",
            "4":"Dividir"
        }
        
        if opcion in ["1","2","3","4"]:
            return opcion
        else:
            print("Invalido")
        # try:
        #     opcion_valida[opcion]
        # except KeyError:
        #     print("Opcion invalida, elgí entre 1 y 4")
        
        # return opcion



def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Deber ingresar un numero válido")



