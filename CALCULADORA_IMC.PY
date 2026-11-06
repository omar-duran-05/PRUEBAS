#SE DECLARA LA VARIABLE NOMBRE JUNTO CON UN BUCLE DE VALIDACION PARA QUE EL USUARIO INGRESE SU NOMBRE, SI NO LO HACE SE LE SOLICITARA NUEVAMENTE HASTA QUE INGRESE UN NOMBRE VALIDO
while True:
    nombre = input("Ingrese su nombre: ").strip().title()
    if nombre == "":
        print("ERROR: No puede dejar el campo vacio")

    elif not nombre.replace(" ", "").isalpha():
        print( "ERROR: Solamente se permiten letras")
    else:
        break

#SE DECLARA LA VARIABLE APELLIDO PATERNO JUNTO CON UN BUCLE DE VALIDACION PARA QUE EL USUARIO INGRESE SU APELLIDO PATERNO, SI NO LO HACE SE LE SOLICITARA NUEVAMENTE HASTA QUE INGRESE UN APELLIDO VALIDO
while True:
    apellido_paterno = input("Ingrese su Apellido Paterno:  ").strip().title()
    if apellido_paterno == "":
        print("ERROR: No puede dejar el campo vacio")
    elif not apellido_paterno.replace(" ", "").isalpha():
        print("ERROR: solamente se permiten letras")
    else:
        break

#SE DECLARA LA VARIABLE APELLIDO MATERNO JUNTO CON UN BUCLE DE VALIDACION PARA QUE EL USUARIO INGRESE SU APELLIDO MATERNO, SI NO LO HACE SE LE SOLICITARA NUEVAMENTE HASTA QUE INGRESE UN APELLIDO VALIDO
while True:
    apellido_materno = input("Ingrese su Apellido Materno: ").strip().title()
    if apellido_materno == "":
        print("ERROR: No puede dejar el campo vacio")
    elif not apellido_materno.replace(" ", "").isalpha():
        print("ERROR: solamente se permiten letras")
    else:
        break

#SE DECLARA LA VARIABLE EDAD JUNTO CON UN BUCLE DE VALIDACION PARA QUE EL USUARIO INGRESE SU EDAD, SI NO LO HACE SE LE SOLICITARA NUEVAMENTE HASTA QUE INGRESE UNA EDAD VALIDA
while True:
    try:
     edad = int(input("Ingrese su edad: "))
     if edad <= 0 or edad > 120:
        print("ERROR: La edad dede ser mayor que cero y menor que 120")
     else:
        break
    except ValueError:
        print("ERROR: Ingrese un numero valido")
    
#SE DECLARA LA VARIABLE PESO JUNTO CON UN BUCLE DE VALIDACION PARA QUE EL USUARIO INGRESE SU PESO, SI NO LO HACE SE LE SOLICITARA NUEVAMENTE HASTA QUE INGRESE UN PESO VALIDO
while True:
    try:
        peso = float(input("Ingrese su peso en kg: "))
        if peso <= 0:
            print("ERROR: El peso debe ser mayor a cero")
        else:
            break
    except ValueError:
        print("ERROR: Ingrese un numero valido")

#SE DECLARA LA VARIABLE ALTURA JUNTO CON UN BUCLE DE VALIDACION PARA QUE EL USUARIO INGRESE SU ALTURA, SI NO LO HACE SE LE SOLICITARA NUEVAMENTE HASTA QUE INGRESE UNA ALTURA VALIDA
while True:
    try: 
        altura = float(input("Ingrese su altura en metros: "))
        if altura <= 0:
            print("ERROR: La altura debe ser mayor a cero")
        else:
            break
    except ValueError:
       print("ERROR: Ingrese un numero valido")

imc = peso / (altura ** 2)


#IMPRESION DE DATOS GUARDADOS EN VARIABLES
print(f"Hola {nombre} {apellido_paterno} {apellido_materno}, tu edad es {edad} años, tu peso es {peso} kg y tu altura es {altura} metros.")

#MOSTRAR RESULTADO DEL IMC CON DOS DECIMALES
print(f"\nTu IMC es: {imc:.2f}")

# Clasificación del IMC
if imc < 18.5:
    print("Clasificación: Bajo peso")

elif imc < 25:
    print("Clasificación: Peso normal")

elif imc < 30:
    print("Clasificación: Sobrepeso")

else:
    print("Clasificación: Obesidad")