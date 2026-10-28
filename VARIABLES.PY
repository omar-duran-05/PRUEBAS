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