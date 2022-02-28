# Los alumnos de un curso se han dividido en dos grupos A y B 
# de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde. 
def buscarGrupo(genero,letraNom):
    if genero=="F":
        if letraNom < "M":
            grupo ="A"
        else:
            grupo ="B"
    elif genero =="M":
        if letraNom>"N":
            grupo="A"
        else:
            grupo="B"
        return "Grupo"+ grupo


sexo=input("ingrese el Sexo del alumno (F/M): ")
nombre=input("Ingresa el nombre del Alumno")
asignacion =buscarGrupo(sexo,nombre[0].upper)
print("el grupo asignado a ",nombre , "es el  -> ", asignacion)