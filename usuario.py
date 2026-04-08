from linked_list import LinkedList
lista = LinkedList()
start = 1

while start != 0:
    print("""Seleccione la opcion que desee realizar:
1. Insertar dato al inicio
2. Insertar dato al final
3. Eliminar primer nodo
4. Eliminar nodo por valor
5. Buscar dato
6. Recorrer lista
7. Ordenar lista
8. Invertir lista
9. Obtener tamaño
10. Salir
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
        result = lista.eliminar_inicio()
        if result:
            print(result)
        else:
            print("Dato eliminado correctamente.")
    elif o == 4:
        valor = float(input("Ingrese el valor que desee eliminar: "))
        result = lista.eliminar_por_valor(valor)
        if result:
            print(result)
        else:
            print("Dato eliminado correctamente.")
    elif o == 5:
        obj = float(input("Ingrese el dato que desee buscar: "))
        encontrado = lista.buscar(obj)
        if encontrado:
            print("Dato encontrado en la lista.")
        else:
            print("Dato no encontrado.")
    elif o == 6:
        lista.recorrer()
    elif o == 7:
        lista.ordenar()
        print("Lista ordenada.")
    elif o == 8:
        lista.invertirLista(lista)
        print("Lista invertida.")
    elif o == 9:
        tamaño = lista.tamañoLista(lista)
        print(f"El tamaño de la lista es: {tamaño}")
    elif o == 10:
        start = 0
        print("Hasta luego.")
    else:
        print("Ingrese un numero valido.")

