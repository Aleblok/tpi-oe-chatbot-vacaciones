# TPI ORGANIZACIÓN EMPRESARIAL – CHATBOT DE GESTIÓN DE VACACIONES

## Descripción

Este proyecto corresponde al Trabajo Práctico Integrador de la materia Organización Empresarial de la Tecnicatura Universitaria en Programación (UTN).

Se desarrolló un simulador de chatbot para automatizar el proceso administrativo de solicitud de vacaciones del personal en una empresa ficticia llamada TecnoGestión S.R.L.

El objetivo principal es demostrar la coherencia entre el modelo de proceso BPMN y la lógica implementada en el código.

## Proceso seleccionado

Gestión de solicitudes de vacaciones del personal.

## Tecnologías utilizadas

* Python 3
* Archivos CSV
* Git y GitHub
* BPMN 2.0
* Máquina de Estados simulada

## Archivos del proyecto

* `main.py`: código principal del chatbot.
* `empleados.csv`: base de datos simulada de empleados.
* `solicitudes.csv`: registro de solicitudes procesadas.
* `README.md`: documentación básica del proyecto.

## Funcionamiento del bot

El chatbot solicita al usuario:

1. Legajo del empleado.
2. Fecha de inicio de vacaciones.
3. Fecha de fin de vacaciones.

Luego el sistema:

1. Valida si el legajo existe.

2. Valida el formato de fechas.

3. Calcula los días solicitados.

4. Consulta los días disponibles del empleado.

5. Determina el estado de la solicitud:

   * APROBADA
   * RECHAZADA
   * PENDIENTE_SUPERVISOR

6. Registra la solicitud en `solicitudes.csv`.

## Reglas de decisión

* Si el legajo no existe, el sistema informa el error.
* Si la fecha es inválida, el sistema informa el formato correcto.
* Si la fecha de fin no es posterior a la fecha de inicio, la solicitud no continúa.
* Si el empleado no tiene días suficientes, la solicitud queda RECHAZADA.
* Si el empleado tiene días suficientes y solicita hasta 10 días, queda APROBADA.
* Si el empleado tiene días suficientes pero solicita más de 10 días, queda PENDIENTE_SUPERVISOR.

## Organización del trabajo en GitHub

El proyecto fue desarrollado utilizando Git y GitHub como herramientas de control de versiones.

Se creó una rama `desarrollo` como rama de integración del proyecto. A partir de ella, se trabajaron las funcionalidades principales en ramas separadas, que luego fueron integradas mediante Pull Requests.

Ramas utilizadas:

* `estructura-inicial`
* `validacion-fechas`
* `reglas-aprobacion`
* `registro-solicitudes`

Esta organización permitió dividir el trabajo por etapas, registrar los cambios realizados y mantener una trazabilidad entre el desarrollo del código y el proceso modelado.

## Ejecución

Para ejecutar el simulador:

```bash
python main.py
```

## Integrantes

* Alessandra Borges Licciardi
* Lautaro Borges Licciardi

