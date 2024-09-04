
print(" CALCULADORA SIMPLE ")

numero1= float(input("ingresa el primer numero:"))
operador= input("ingresa el operador que quieras realizar (+,-,*,/):")
nuemro2= float(input("ingresa el segundo numero:"))

if operador == "+":
    resultado= numero1+nuemro2
    print(f"el resultado de la suma es:{resultado}")
elif operador == "-":
    resultado = numero1-nuemro2
    print(f" el resultado de la resta fue: {resultado}")
elif operador == "*":
    resultado = numero1* nuemro2
    print(f"el resultado de la multiplicacion es: {resultado}")
elif operador == "/":
    if nuemro2 != 0:
            resultado = numero1 / nuemro2
            print("Resultado:", resultado)
    else:
            print("Error: No se puede dividir por cero.")
else:
        print("Operador no válido")
   

