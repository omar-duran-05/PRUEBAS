
#VARIABLE PARA NOMBRE 
nombre = input("Ingrese su nombre: ")

#VARIABLE PARA APELLIDO PATERNO 
apellido_paterno = input("Ingrese su apellido paterno: ")

#VARIABLE PARA APELLIDO MATERNO 
apellido_materno = input("Ingrese su apellido materno: ")

#VARIBALE PARA EDAD 
edad = int(input("Ingrese su edad: "))
#LA VARIABLE QUE USE EN ESTE CASO ES INT PORQUE LA EDAD ES UN NUMERO ENTERO, SI FUERA DECIMAL SE USARIA FLOAT

#VARIABLE PARA PESO
peso = float(input("Ingrese su peso en kg: "))
#LA VARIABLE QUE USE EN ESTE CASO ES FLOAT PORQUE EL PESO PUEDE SER UN NUMERO DECIMAL, SI FUERA ENTERO SE USARIA INT

#VARIABLE PARA ALTURA   
altura = float(input("Ingrese su altura en metros: "))
#LA VARIABLE QUE USE EN ESTE CASO ES FLOAT PORQUE LA ALTURA PUEDE SER UN NUMERO DECIMAL, SI FUERA ENTERO SE USARIA INT

#IMPRESION DE DATOS GUARDADOS EN VARIABLES
print(f"Hola {nombre} {apellido_paterno} {apellido_materno}, tu edad es {edad} años, tu peso es {peso} kg y tu altura es {altura} metros.")