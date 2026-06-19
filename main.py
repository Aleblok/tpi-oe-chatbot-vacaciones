import csv
import datetime


def cargar_empleados():
    empleados = {}

    with open("empleados.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            empleados[fila["legajo"]] = fila

    return empleados


def validar_fecha(texto):
    try:
        dia, mes, anio = texto.split("/")
        fecha = datetime.date(int(anio), int(mes), int(dia))
        return fecha
    except ValueError:
        return None


def evaluar_solicitud(dias_solicitados, dias_disponibles):
    if dias_solicitados > dias_disponibles:
        return "RECHAZADA", "No dispone de suficientes días de vacaciones."

    if dias_solicitados > 10:
        return "PENDIENTE_SUPERVISOR", "La solicitud será derivada a supervisión para su evaluación."

    return "APROBADA", "Solicitud aprobada automáticamente."


def main():
    print("=== CHATBOT DE GESTIÓN DE VACACIONES ===")

    empleados = cargar_empleados()

    legajo = input("Ingrese su legajo: ").strip()

    if legajo in empleados:
        empleado = empleados[legajo]

        print(f"Bienvenido/a {empleado['nombre']} {empleado['apellido']}")
        print(f"Días disponibles: {empleado['dias_vacaciones']}")

        fecha_inicio_texto = input("Ingrese fecha de inicio (dd/mm/yyyy): ").strip()
        fecha_inicio = validar_fecha(fecha_inicio_texto)

        if fecha_inicio is None:
            print("Fecha de inicio inválida. Use el formato dd/mm/yyyy.")
            return

        fecha_fin_texto = input("Ingrese fecha de fin (dd/mm/yyyy): ").strip()
        fecha_fin = validar_fecha(fecha_fin_texto)

        if fecha_fin is None:
            print("Fecha de fin inválida. Use el formato dd/mm/yyyy.")
            return

        if fecha_fin <= fecha_inicio:
            print("La fecha de fin debe ser posterior a la fecha de inicio.")
            return

        dias_solicitados = (fecha_fin - fecha_inicio).days
        dias_disponibles = int(empleado["dias_vacaciones"])

        estado, observacion = evaluar_solicitud(dias_solicitados, dias_disponibles)

        print("Solicitud procesada correctamente.")
        print(f"Fecha de inicio: {fecha_inicio_texto}")
        print(f"Fecha de fin: {fecha_fin_texto}")
        print(f"Días solicitados: {dias_solicitados}")
        print(f"Estado: {estado}")
        print(f"Observación: {observacion}")

    else:
        print("Legajo no encontrado.")


main()