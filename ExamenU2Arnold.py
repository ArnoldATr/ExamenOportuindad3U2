# Arnold Avalos Torres
# No. Control: 18420428
# Fecha 23/Octubre/2022
import json

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

def jsonbien():
    con = []
    i = 0
    while i <= len(contactos[0]):
        dicc = {}
        dicc["nombre"] = contactos[i][0]
        dicc["funcion"] = contactos[i][1]
        dicc["correo"] = contactos[i][2]
        con.append(dicc)
        i = i + 1
    return con

    try:
        con = jsonbien()
    except:
        print("Hay un error, lo siento...")
        list = json.dumps(con)
        print(list)

print(jsonbien())






