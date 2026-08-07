ids = []
nombres = []
usuarios = []
contrasenas = []
correos = []
roles = []
estados = []
fechas = []
ultimos_accesos = []
intentos = []
#---------------------------------------------#
#--|menu_principal_autenticador_de_usuarios|--#
#---------------------------------------------#
while True:
    print("menu principal autenticador de usuarios")
    print("1) registrar usuario")
    print("2) iniciar sesión")
    print("3) editar usuario")
    print("4) eliminar usuario")
    print("5) buscar usuario")
    print("6) lista de datos")
    print("7) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------#
    #--|registrar_usuario|--#
    #-----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_usuario = 1
        else:
            id_usuario = ids[-1] + 1
        nombre = input("nombre: ")
        usuario = input("usuario: ")
        contrasena = input("contraseña: ")
        correo = input("correo: ")
        rol = input("rol: ")
        fecha = input("fecha de registro: ")
        estado = "activo"
        ids.append(id_usuario)
        nombres.append(nombre)
        usuarios.append(usuario)
        contrasenas.append(contrasena)
        correos.append(correo)
        roles.append(rol)
        estados.append(estado)
        fechas.append(fecha)
        ultimos_accesos.append("sin registros")
        intentos.append(0)
        print("usuario registrado correctamente.")
        print("id:", id_usuario)
        print("estado:", estado)
    #--------------------#
    #--|iniciar_sesion|--#
    #--------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen usuarios registrados.")
        else:
            print("inicio de sesión")
            usuario_ingreso = input("usuario: ")
            contrasena_ingreso = input("contraseña: ")
            encontrado = False
            for i in range(len(ids)):
                if usuarios[i] == usuario_ingreso:
                    encontrado = True
                    if estados[i].lower() == "bloqueado":
                        print("usuario bloqueado.")
                        print("acceso denegado.")
                    else:
                        if contrasenas[i] == contrasena_ingreso:
                            intentos[i] = 0
                            ultimos_accesos[i] = "acceso correcto"
                            print("autenticación correcta.")
                            print("acceso permitido.")
                            print("bienvenido:", nombres[i])
                        else:
                            intentos[i] += 1
                            print("contraseña incorrecta.")
                            print(
                                "intento:",
                                intentos[i]
                            )
                            if intentos[i] >= 3:
                                estados[i] = "bloqueado"
                                print(
                                    "usuario bloqueado por "
                                    "demasiados intentos."
                                )
                    break
            if encontrado == False:
                print("usuario no encontrado.")
    #--------------------#
    #--|editar_usuario|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen usuarios registrados.")
        else:
            print("editar usuario")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{usuarios[i]} | "
                    f"{roles[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id del usuario: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("nombre:", nombres[posicion])
                print("usuario:", usuarios[posicion])
                print("correo:", correos[posicion])
                print("rol:", roles[posicion])
                print("estado:", estados[posicion])
                nombres[posicion] = input(
                    "nuevo nombre: "
                )
                usuarios[posicion] = input(
                    "nuevo usuario: "
                )
                contrasenas[posicion] = input(
                    "nueva contraseña: "
                )
                correos[posicion] = input(
                    "nuevo correo: "
                )
                roles[posicion] = input(
                    "nuevo rol: "
                )
                fechas[posicion] = input(
                    "nueva fecha: "
                )
                print(
                    "usuario actualizado correctamente."
                )
            else:
                print("id no encontrada.")
    #----------------------#
    #--|eliminar_usuario|--#
    #----------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen usuarios registrados.")
        else:
            print("eliminar usuario")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{usuarios[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id del usuario: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print(
                    "usuario:",
                    usuarios[posicion]
                )
                confirmacion = input(
                    "¿desea eliminar usuario? (s/n): "
                )
                if confirmacion.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    usuarios.pop(posicion)
                    contrasenas.pop(posicion)
                    correos.pop(posicion)
                    roles.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    ultimos_accesos.pop(posicion)
                    intentos.pop(posicion)
                    print(
                        "usuario eliminado correctamente."
                    )
                else:
                    print(
                        "usuario no eliminado."
                    )
            else:
                print("id no encontrada.")
    #--------------------#
    #--|buscar_usuario|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen usuarios registrados.")
        else:
            id_buscar = int(
                input("ingrese la id del usuario: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("información del usuario")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("usuario:", usuarios[posicion])
                print("contraseña: ********")
                print("correo:", correos[posicion])
                print("rol:", roles[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print(
                    "último acceso:",
                    ultimos_accesos[posicion]
                )
                print(
                    "intentos:",
                    intentos[posicion]
                )
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "6":
        if len(ids) == 0:
            print("no existen usuarios registrados.")
        else:
            activos = 0
            bloqueados = 0
            pendientes = 0
            administradores = 0
            usuarios_normales = 0
            invitados = 0
            accesos_correctos = 0
            accesos_fallidos = 0
            print("lista de usuarios")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{usuarios[i]} | "
                    f"{roles[i]} | "
                    f"{estados[i]}"
                )
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "bloqueado":
                    bloqueados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
                if roles[i].lower() == "administrador":
                    administradores += 1
                elif roles[i].lower() == "usuario":
                    usuarios_normales += 1
                elif roles[i].lower() == "invitado":
                    invitados += 1
                if ultimos_accesos[i] == "acceso correcto":
                    accesos_correctos += 1
                if intentos[i] > 0:
                    accesos_fallidos += intentos[i]
            print("estadísticas autenticador de usuarios")
            print("cantidad usuarios:", len(ids))
            print("usuarios activos:", activos)
            print("usuarios bloqueados:", bloqueados)
            print("usuarios pendientes:", pendientes)
            print("roles")
            print("administradores:", administradores)
            print("usuarios:", usuarios_normales)
            print("invitados:", invitados)
            print("accesos")
            print(
                "accesos correctos:",
                accesos_correctos
            )
            print(
                "intentos fallidos:",
                accesos_fallidos
            )
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "7":
        print(
            "gracias por utilizar el autenticador de usuarios."
        )
        break
    else:
        print("opción no válida.")