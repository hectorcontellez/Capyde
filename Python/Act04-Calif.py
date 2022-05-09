edad = int(input("Escribe tu edad: "))
calificacion = int(input("Escribe tu calificación: "))
nivel = input("Escribe tu nivel de estudios (Bachiller / Universidad): ")

if edad > 17:
    textoEdad = "Eres mayor de edad "
else:
    textoEdad = "Eres menor de edad "

if calificacion > 5:
    textoCalificacion = "aprobaste "
else:
    textoCalificacion = "reprobaste "

print(textoEdad,"y tienes ",edad,"años, ",textoCalificacion,"la materia con ",calificacion,"del nivel ",nivel)