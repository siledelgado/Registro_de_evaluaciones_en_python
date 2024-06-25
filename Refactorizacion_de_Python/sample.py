def mostrar_resultados():
    # Función para mostrar los resultados guardados en el archivo "data.txt"
    print('Resultados hasta la fecha.')
    archivo_lectura = open("data.txt", "r")  # Abre el archivo en modo lectura
    print(archivo_lectura.read())  # Lee y muestra todo el contenido del archivo
    archivo_lectura.close()  # Cierra el archivo

def ingresar_comentarios():
    # Función para ingresar una puntuación y un comentario
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5:')
        puntuacion = input()  # Recibe la puntuación como entrada del usuario
        if puntuacion.isdecimal():  # Verifica si la entrada es un número decimal
            puntuacion = int(puntuacion)  # Convierte la puntuación a un entero
            if puntuacion <= 0 or puntuacion > 5:  # Verifica si la puntuación está fuera del rango permitido
                print('Indíquelo en una escala de 1 a 5:')  # Solicita al usuario una puntuación válida
            else:
                print('Introduzca sus comentarios.')  # Solicita un comentario al usuario
                comentario = input()  # Recibe el comentario como entrada del usuario
                entrada = f'puntuación: {puntuacion} comentario: {comentario}'  # Formatea la entrada
                archivo_escritura = open("data.txt", 'a')  # Abre el archivo en modo de anexar (agregar al final)
                archivo_escritura.write(f'{entrada}\n')  # Escribe la entrada formateada en el archivo
                archivo_escritura.close()  # Cierra el archivo
                break  # Sale del bucle al completar la entrada
        else:
            print('Por favor, ingrese la puntuación como un número:')  # Solicita al usuario que ingrese un número

while True:
    # Bucle principal que muestra el menú y maneja la selección del usuario
    print('Seleccione el proceso que desea aplicar.')
    print('1: Ingresar puntuaciones y comentarios.')
    print('2: Verificar los resultados obtenidos hasta ahora.')
    print('3: Salir.')
    opcion = input()  # Recibe la selección del usuario

    if opcion.isdecimal():  # Verifica si la selección es un número
        opcion = int(opcion)  # Convierte la selección a un entero
        if opcion == 1:
            ingresar_comentarios()  # Llama a la función para ingresar comentarios
        elif opcion == 2:
            mostrar_resultados()  # Llama a la función para mostrar resultados
        elif opcion == 3:
            print('Saliendo.')  # Muestra un mensaje de salida
            break  # Sale del bucle, terminando el programa
        else:
            print('Por favor, introduzca un número del 1 al 3.')  # Solicita una opción válida al usuario
    else:
        print('Por favor, introduzca un número del 1 al 3.')  # Solicita una opción válida al usuario
