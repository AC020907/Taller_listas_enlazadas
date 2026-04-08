from linked_list import LinkedList

lista = LinkedList()
start = 1

while start != 0:
    print("""Seleccione la opcion que desee realizar:
1. Insertar dato al inicio
2. Insertar dato al final
3. Buscar dato
4. Recorrer lista
8. Ordenar lista
9. Salir
""")
    o = int(input("Opcion: "))

    if o == 1:
        data = float(input("Ingrese el dato que desee insertar al inicio: "))
        lista.insertar_inicio(data)
        print("Se inserto el dato correctamente.")
    elif o == 2:
        data = float(input("Ingrese el dato que desee insertar al final: "))
        lista.insertar_final(data)
        print("Se inserto el dato correctamente.")
    elif o == 3:
        obj = float(input("Ingrese el dato que desee buscar: "))
        encontrado = lista.buscar(obj)
        if encontrado:
            print("Dato encontrado en la lista.")
        else:
            print("Dato no encontrado.")
    elif o == 4:
        lista.recorrer()
    elif o== 8:
        lista.ordenar()
    elif o == 9:
        start = 0
    else:
        print("Ingrese un numero valido.")

