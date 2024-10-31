def cargar_secuencialmente():
    alumnos = []
    cargar = True
    while cargar:
    
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        comision = input("Ingrese la comision:")
        carrera = input("Ingrese la carrera: ")
        curso = (comision, carrera)

        alumno = {
            "Nombre": nombre,
            "Apellido": apellido,
            "Edad": edad,
            "Curso": curso
        }

        alumnos.append(alumno)

        seguir = input("Quiere seguir cargando alumnos? s/n: ")

        while seguir != "s" and seguir != "n":
            seguir = input("Quiere seguir cargando alumnos? s/n: ")

        cargar = seguir == "s"
    
    return alumnos

