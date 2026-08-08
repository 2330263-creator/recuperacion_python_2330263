import sys
from recuperacion_python_2330263.services import GimnasioService


def mostrar_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA DE GESTIÓN DE GIMNASIO    ")
    print("=" * 40)
    print("1. Registrar nuevo socio")
    print("2. Mostrar todos los socios")
    print("3. Buscar socio por ID")
    print("4. Actualizar socio")
    print("5. Eliminar socio")
    print("6. Calcular ingreso mensual esperado")
    print("7. Filtrar socios por tipo de membresía")
    print("8. Mostrar edad promedio de los socios")
    print("9. Mostrar resumen general")
    print("0. Salir")
    print("=" * 40)


def main():
    service = GimnasioService()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Registrar Socio ---")
            id_socio = input("ID único: ")
            nombre = input("Nombre completo: ")
            try:
                edad = int(input("Edad: "))
                print("Tipos de membresía válidos: Básica, Premium, VIP")
                membresia = input("Membresía: ")
                mensualidad = float(input("Mensualidad ($): "))
                socio = service.registrar_socio(
                    id_socio, nombre, edad, membresia, mensualidad
                )
                print(f"¡Socio '{socio.nombre}' registrado con éxito!")
            except ValueError as e:
                print(f"Error al registrar: {e}")

        elif opcion == "2":
            print("\n--- Lista de Socios ---")
            socios = service.obtener_todos()
            if not socios:
                print("No hay socios registrados en el sistema.")
            else:
                for s in socios:
                    print(
                        f"ID: {s.id_socio} | Nombre: {s.nombre} | Edad: {s.edad} | "
                        f"Membresía: {s.membresia} | Mensualidad: ${s.mensualidad:.2f}"
                    )

        elif opcion == "3":
            print("\n--- Buscar Socio por ID ---")
            id_socio = input("Ingrese el ID del socio: ")
            socio = service.buscar_por_id(id_socio)
            if socio:
                print(
                    f"\nEncontrado: {socio.nombre} | Edad: {socio.edad} | "
                    f"Membresía: {socio.membresia} | Mensualidad: ${socio.mensualidad:.2f}"
                )
            else:
                print(f"No se encontró ningún socio con el ID '{id_socio}'.")

        elif opcion == "4":
            print("\n--- Actualizar Socio ---")
            id_socio = input("Ingrese el ID del socio a actualizar: ")
            socio = service.buscar_por_id(id_socio)
            if not socio:
                print("Socio no encontrado.")
                continue

            print("Presione ENTER para mantener el valor actual.")
            nombre = input(f"Nuevo nombre [{socio.nombre}]: ").strip() or None
            edad_str = input(f"Nueva edad [{socio.edad}]: ").strip()
            edad = int(edad_str) if edad_str else None

            membresia = (
                input(f"Nueva membresía [{socio.membresia}]: ").strip() or None
            )
            mensualidad_str = input(
                f"Nueva mensualidad [${socio.mensualidad}]: "
            ).strip()
            mensualidad = float(mensualidad_str) if mensualidad_str else None

            try:
                if service.actualizar_socio(
                    id_socio, nombre, edad, membresia, mensualidad
                ):
                    print("Socio actualizado con éxito.")
            except ValueError as e:
                print(f"Error al actualizar: {e}")

        elif opcion == "5":
            print("\n--- Eliminar Socio ---")
            id_socio = input("Ingrese el ID del socio a eliminar: ")
            if service.eliminar_socio(id_socio):
                print(f"Socio con ID '{id_socio}' eliminado correctamente.")
            else:
                print("No se encontró ningún socio con ese ID.")

        elif opcion == "6":
            total = service.calcular_ingreso_mensual_esperado()
            print(f"\nIngreso mensual esperado total: ${total:.2f}")

        elif opcion == "7":
            print("\n--- Filtrar por Membresía ---")
            tipo = input("Tipo de membresía (Básica / Premium / VIP): ")
            filtrados = service.filtrar_por_membresia(tipo)
            if not filtrados:
                print(f"No hay socios registrados con membresía '{tipo}'.")
            else:
                for s in filtrados:
                    print(
                        f"ID: {s.id_socio} | Nombre: {s.nombre} | Mensualidad: ${s.mensualidad:.2f}"
                    )

        elif opcion == "8":
            promedio = service.calcular_edad_promedio()
            print(f"\nEdad promedio de los socios: {promedio:.1f} años")

        elif opcion == "9":
            resumen = service.obtener_resumen_general()
            print("\n--- Resumen General ---")
            print(f"Total de socios: {resumen['total_socios']}")
            print(
                f"Ingreso mensual esperado: ${resumen['ingreso_mensual_esperado']:.2f}"
            )
            print(f"Edad promedio: {resumen['edad_promedio']} años")

        elif opcion == "0":
            print("\n¡Gracias por utilizar el sistema!")
            sys.exit(0)
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()