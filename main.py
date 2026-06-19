import csv


def cargar_empleados():
    empleados = {}

    with open("empleados.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            empleados[fila["legajo"]] = fila

    return empleados


def main():
    print("=== CHATBOT DE GESTIÓN DE VACACIONES ===")

    empleados = cargar_empleados()

    legajo = input("Ingrese su legajo: ")

    if legajo in empleados:
        empleado = empleados[legajo]

        print(f"Bienvenido/a {empleado['nombre']} {empleado['apellido']}")
        print(
            f"Días disponibles: {empleado['dias_vacaciones']}"
        )

    else:
        print("Legajo no encontrado.")


main()