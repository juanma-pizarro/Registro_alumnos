# Los alumnos
alumnos = {}

# Las funcines para ver el registro
def nuevo_alumno():
    while True:
        id = input('Ingrese el RUN del alumno  [0 para terminar]: ')
        if id=='0':
            break
        notas = []
        try:
            cantidad_notas = int(input('Ingrese la cantidad de notas del alumno: '))
            for n in range(cantidad_notas):
                nota = float(input(f'Ingrese la nota {n+1}: '))
                notas.append(nota)
            alumnos[id] = notas
            print('alumno creado exitosamente.')
        except:
            print('Error. Intente nuevamente')

def buscador_notas(): 
    id = input('Ingrese el RUN del alumno: ')
    if id in alumnos:
        notas = alumnos[id]
        promedio = sum(notas) / len(notas)
        print(f'Notas del alumno: {notas}')
        print(f'Promedio del alumno: {promedio}')
    else:
        print('El alumno no existe.')

def calcular_promedio():
    for id , notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f'El promedio del alumno {id}: {promedio}')

def borrar_alumno():
    id = input('Ingrese el RUN del alumno: ')
    if id in alumnos:
        del alumnos[id]
        print('alumno borrado de la lista.')
    else:
        print('El alumno no existe.')

def actualizar_notas():
    id = input('Ingrese el RUN del alumno: ')
    if id in alumnos:
        notas = alumnos[id]
        try:
            cantidad_notas = int(input('Ingrese la cantidad de notas del alumno: '))
        except:
            print('Intente nuevamente.')
            notas.clear()
            for i in range(cantidad_notas):
                nota = float(input(f'Ingrese la nota {i+1}: '))
                notas.append(nota)
            print('Notas actualizadas exitosamente.')
    else:
        print('El alumno no existe.')

def listar_alumnos():
    for id, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f'Alumno: {id}')
        print(f'Notas: {notas}')
        print(f'Promedio: {promedio}')
        print()

def mostrar_repitentes():
    for id, notas in alumnos.items():
        if len(notas) > 0 in all(nota < 4.0 for nota in notas):
            print(f'Alumno repitente: {id}')

def mostrar_aprobados():
    for id, notas in alumnos.items():
        if len(notas) > 0 in all(nota >= 4.0 for nota in notas):
            print(f'Alumno aprobado: {id}')


def importar_alumnos():
    archivo = input("Ingrese el nombre del archivo TXT: ")
    try:
        with open(archivo, 'r') as file:
            for line in file:
                identificador, *notas = line.strip().split(',')
                notas = list(map(float, notas))
                alumnos[identificador] = notas
        print('Alumnos importados exitosamente.')
    except FileNotFoundError:
        print('El archivo no existe.')

def exportar_alumno():
    archivo = input('Ingrese el nombre del arichivo TXT: ')
    directorio = open(f'{archivo}.txt', 'a')
    for key,value in alumnos.items():
        directorio.write(f'{key} {value}')
        
    directorio.close

# Menu del profesor 
while True:
    print('----- Registro -----')
    print('[1] Nuevo alumno')
    print('[2] Buscar notas del alumno y su promedio')
    print('[3] Calcular el promedio de notas de cada alumno')
    print('[4] Borrar a un alumno')
    print('[5] Actualizar las notas de un alumno')
    print('[6] Listar todos los alumnos con notas y el promedio final')
    print('[7] Mostrar alumnos repitentes')
    print('[8] Mostrar alumnos aprobados')
    print('[9] Importar todos los alumnos a un documento TXT')
    print('[10] Exportar los alumnos del documento TXT al programa')
    print('[0] Salir')

# Realiza la opcion seleccionada
    opc = input('Ingrese una opcion: ')

    if opc == '1':
        nuevo_alumno()
    elif opc == '2':
        buscador_notas()
    elif opc == '3':
        calcular_promedio()
    elif opc == '4':
        borrar_alumno()
    elif opc == '5':
        actualizar_notas()
    elif opc == '6':
        listar_alumnos()
    elif opc == '7':
        mostrar_repitentes()
    elif opc == '8':
        mostrar_aprobados()
    elif opc == '9':
        importar_alumnos()
    elif opc == '10':
        exportar_alumno()
    elif opc == '0':
        print('\nJuan Manuel Pizarro.')
        print('Python.')
        break
    else:
        print('Opción inválida. Intente nuevamente.')