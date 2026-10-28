#Variable integer
chocolate = 50

#Variable float
PI = 3.141592653589793

#Variable boolean 
is_active = True

#Variable string/char
saludo = "HOLA , MUNDO!"

print(f"variables simples: {chocolate}, {PI}, {is_active}, {saludo}") 


#---------------------

#variable list
#[index0, index1, index2, ......]
fruits = ["apple", "banana", "cherry"]

#variable tuple
#(value0, value1, value2, ......)
coordinates = (10.0, 20.0, 30.0)

#variable dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming"]
}

print(f"variables compuestas: {fruits}, {coordinates}, {person}")


print (fruits [1]) #acceder a un elemento de la lista
print (coordinates [2]) #acceder a un elemento de la tupla
print (person ["city"]) #acceder a un elemento del diccionario
print (person ["hobbies"] [0]) #acceder a un elemento de la lista dentro del diccionario


#---------------------

#ejmplo de conversion de tipos de datos
numero_str = "100"

#a + b deber de ser el mimo tipo de dato (entero o decimal)
#no podemos sumar o concatenar un string con un entero directamente
print (f"{numero_str}50") #output: 10050 

numero_int = int(numero_str) #convertimos el string a entero
print (numero_int + 50) #output: 150

fruits_str = ["10", "20", "30"]
print (fruits_str) #output: ['10', '20', '30']

fruits_int = list(map(int, fruits_str)) #convertimos la lista de strings a lista de enteros
print (fruits_int) #output: [10, 20, 30]

flotante = 25.657
entero = int(flotante) #convertimos el float a entero
print (entero) #output: 25
print (int(round(flotante, 0))) #output: 26
print (round(flotante, 0)) #output: 26.0


flotante_nuevo = float(numero_str) #convertimos entero a float
print (flotante_nuevo) #output: 100.0
print (entero + flotante_nuevo) #output: 125.0


#conversion de boleano
is_boolean = True 
is_boolean_str = str(is_boolean) #convertimos booleano a string
print (is_boolean_str) #output: True
is_boolean_int = int(is_boolean) #convertimos booleano a entero
print (is_boolean_int) #output: 1
is_boolean_float = float(is_boolean) #convertimos booleano a float
print (is_boolean_float) #output: 1.0
boolean_float = bool(is_boolean_float) #convertimos float a booleano
print (boolean_float) #output: True