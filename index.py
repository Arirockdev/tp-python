# variables del menu

agregar_producto = 1
mostrar_lista = 2
salir_del_programa = 3
lista_productos = []


while True:

# Menu de opciones 
  print(f"""\nSeleccione una opcion:
      1-{agregar_producto} para agregar un articulo
      2-{mostrar_lista} para mostrar todos lo productos
      3-{salir_del_programa} para salir\n""")

  opcion_elegida = float(input('\ningresa una opcion: '))

  if opcion_elegida == agregar_producto :

    producto = input('\nagrega el producto: ')
    cantidad = input('\nagrega la cantidad: ')

    producto_encontrado = False

    for item in lista_productos :
      if item["producto"] == producto :
        item["cantidad"] = cantidad     
        producto_encontrado = True
        break


    if not producto_encontrado :
        lista_productos.append({"producto": producto, "cantidad": cantidad})
        print("\nProducto agregado")

  elif opcion_elegida == mostrar_lista:

    print(f"\n{lista_productos}")

  elif opcion_elegida == salir_del_programa :

    print(f"elegiste la opcion salir del programa")
    break

print('fin de la ejecución')


