"""Aplicación sencilla para gestionar reservas de entradas de cine."""

import os
import sys

# ESTRUCTURA DEL PROGRAMA
#
# main()
# └── procesar_opcion()
#     ├── ejecutar_reserva()
#     │   ├── pedir_cantidad()
#     │   └── reservar_entradas()
#     │       ├── calcular_disponibles()
#     │       └── calcular_importe()
#     ├── ejecutar_cancelacion()
#     │   ├── pedir_cantidad()
#     │   └── cancelar_entradas()
#     │       └── calcular_importe()
#     ├── consultar_disponibilidad()
#     │   └── calcular_disponibles()
#     ├── consultar_recaudacion()
#     ├── limpiar_pantalla()
#     └── pausar_pantalla()
#

# CONSTANTES

AFORO: int = 50
PRECIO_ENTRADA: float = 7.50

OPCION_RESERVAR: str = "1"
OPCION_CANCELAR: str = "2"
OPCION_DISPONIBILIDAD: str = "3"
OPCION_RECAUDACION: str = "4"
OPCION_SALIR: str = "0"

OPCIONES_VALIDAS: tuple[str, ...] = (
    OPCION_RESERVAR,
    OPCION_CANCELAR,
    OPCION_DISPONIBILIDAD,
    OPCION_RECAUDACION,
)

# FUNCIONES DE INTERACCIÓN CON EL USUARIO


def mostrar_menu() -> None:
    """Muestra las opciones disponibles.

    Returns:
        None: Esta función solo muestra información por consola.
    """
    print("\n--- RESERVAS DE CINE ---")
    print(f"{OPCION_RESERVAR}. Reservar entradas")
    print(f"{OPCION_CANCELAR}. Cancelar entradas")
    print(f"{OPCION_DISPONIBILIDAD}. Consultar disponibilidad")
    print(f"{OPCION_RECAUDACION}. Consultar recaudación")
    print(f"{OPCION_SALIR}. Salir")


def pedir_opcion() -> str:
    """Solicita y devuelve una opción del menú.

    Returns:
        str: Opción introducida por el usuario, sin espacios exteriores.
    """
    return input("Selecciona una opción: ").strip()


def pedir_cantidad() -> int:
    """Solicita una cantidad de entradas positiva.

    Returns:
        int: Cantidad de entradas introducida por el usuario.
    """
    cantidad: int = 0
    entrada_valida: bool = False

    while not entrada_valida:
        try:
            cantidad = int(input("Introduce la cantidad de entradas: "))
        except ValueError:
            print("Error: debes introducir un número entero.")
        else:
            if cantidad > 0:
                entrada_valida = True
            else:
                print("Error: la cantidad debe ser mayor que cero.")

    return cantidad


def limpiar_pantalla() -> None:
    """Limpia la pantalla de la consola según el sistema operativo.

    Returns:
        None: Esta función solo modifica el contenido visible de la consola.
    """
    if sys.stdout.isatty():
        comando: str = "cls" if os.name == "nt" else "clear"
        os.system(comando)
    else:
        print("\n" * 50)


def pausar_pantalla() -> None:
    """Pausa el programa hasta que el usuario pulse una tecla y Enter.

    Returns:
        None: Esta función solo espera la interacción del usuario.
    """
    input("\nPulse para continuar....")

# FUNCIONES DE PROCESAMIENTO DE DATOS


def calcular_importe(cantidad: int) -> float:
    """Calcula el importe correspondiente a una cantidad de entradas.

    Args:
        cantidad: Número de entradas cuyo importe se quiere calcular.

    Returns:
        float: Importe total de las entradas.
    """
    return cantidad * PRECIO_ENTRADA


def calcular_disponibles(ocupadas: int) -> int:
    """Calcula el número de entradas disponibles.

    Args:
        ocupadas: Número de entradas reservadas actualmente.

    Returns:
        int: Número de entradas que todavía se pueden reservar.
    """
    return AFORO - ocupadas


def reservar_entradas(
    cantidad: int,
    ocupadas: int,
    recaudacion: float
) -> tuple[int, float]:
    """Procesa una reserva y devuelve el estado actualizado.

    Args:
        cantidad: Número de entradas que se quieren reservar.
        ocupadas: Número actual de entradas reservadas.
        recaudacion: Recaudación acumulada antes de la reserva.

    Returns:
        tuple[int, float]: Nuevas entradas ocupadas y nueva recaudación.

    Raises:
        ValueError: Si la cantidad no es positiva o no hay suficientes
            entradas disponibles.
    """
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    disponibles: int = calcular_disponibles(ocupadas)
    if cantidad > disponibles:
        raise ValueError("No hay suficientes entradas disponibles.")

    importe: float = calcular_importe(cantidad)
    nuevas_ocupadas: int = ocupadas + cantidad
    nueva_recaudacion: float = recaudacion + importe

    return nuevas_ocupadas, nueva_recaudacion


def cancelar_entradas(
    cantidad: int,
    ocupadas: int,
    recaudacion: float
) -> tuple[int, float]:
    """Procesa una cancelación y devuelve el estado actualizado.

    Args:
        cantidad: Número de entradas que se quieren cancelar.
        ocupadas: Número actual de entradas reservadas.
        recaudacion: Recaudación acumulada antes de la cancelación.

    Returns:
        tuple[int, float]: Nuevas entradas ocupadas y nueva recaudación.

    Raises:
        ValueError: Si la cantidad no es positiva o se quieren cancelar más
            entradas de las reservadas.
    """
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    if cantidad > ocupadas:
        raise ValueError(
            "No se pueden cancelar más entradas de las reservadas."
        )

    importe: float = calcular_importe(cantidad)
    nuevas_ocupadas: int = ocupadas - cantidad
    nueva_recaudacion: float = recaudacion - importe

    return nuevas_ocupadas, nueva_recaudacion

# FUNCIONES DE COORDINACIÓN DE OPERACIONES


def ejecutar_reserva(
    ocupadas: int,
    recaudacion: float
) -> tuple[int, float]:
    """Solicita los datos y muestra el resultado de una reserva.

    Args:
        ocupadas: Número actual de entradas reservadas.
        recaudacion: Recaudación acumulada antes de la reserva.

    Returns:
        tuple[int, float]: Nuevas entradas ocupadas y nueva recaudación.

    Raises:
        ValueError: Si la cantidad no es positiva o no hay suficientes
            entradas disponibles.
    """
    cantidad: int = pedir_cantidad()
    nuevas_ocupadas, nueva_recaudacion = reservar_entradas(
        cantidad,
        ocupadas,
        recaudacion
    )

    importe: float = calcular_importe(cantidad)
    print(f"Reserva realizada: {cantidad} entradas.")
    print(f"Importe: {importe:.2f} €")

    return nuevas_ocupadas, nueva_recaudacion


def ejecutar_cancelacion(
    ocupadas: int,
    recaudacion: float
) -> tuple[int, float]:
    """Solicita los datos y muestra el resultado de una cancelación.

    Args:
        ocupadas: Número actual de entradas reservadas.
        recaudacion: Recaudación acumulada antes de la cancelación.

    Returns:
        tuple[int, float]: Nuevas entradas ocupadas y nueva recaudación.

    Raises:
        ValueError: Si la cantidad no es positiva o se quieren cancelar más
            entradas de las reservadas.
    """
    cantidad: int = pedir_cantidad()
    nuevas_ocupadas, nueva_recaudacion = cancelar_entradas(
        cantidad,
        ocupadas,
        recaudacion
    )

    importe: float = calcular_importe(cantidad)
    print(f"Cancelación realizada: {cantidad} entradas.")
    print(f"Importe devuelto: {importe:.2f} €")

    return nuevas_ocupadas, nueva_recaudacion

# FUNCIONES DE CONSULTA


def consultar_disponibilidad(ocupadas: int) -> None:
    """Muestra la información de disponibilidad del cine.

    Args:
        ocupadas: Número actual de entradas reservadas.

    Returns:
        None: Esta función solo muestra información por consola.
    """
    disponibles: int = calcular_disponibles(ocupadas)

    print(f"\nAforo total: {AFORO}")
    print(f"Entradas reservadas: {ocupadas}")
    print(f"Entradas disponibles: {disponibles}")


def consultar_recaudacion(recaudacion: float) -> None:
    """Muestra la recaudación acumulada.

    Args:
        recaudacion: Importe acumulado por las reservas realizadas.

    Returns:
        None: Esta función solo muestra información por consola.
    """
    print(f"\nRecaudación actual: {recaudacion:.2f} €")

# CONTROL DE OPCIONES


def procesar_opcion(
    opcion: str, ocupadas: int, recaudacion: float
) -> tuple[int, float]:
    """Ejecuta la operación asociada a una opción del menú.

    Args:
        opcion: Opción seleccionada en el menú.
        ocupadas: Número actual de entradas reservadas.
        recaudacion: Recaudación acumulada.

    Returns:
        tuple[int, float]: Estado actualizado de entradas y recaudación.
    """
    if opcion == OPCION_RESERVAR:
        ocupadas, recaudacion = ejecutar_reserva(
            ocupadas, recaudacion
        )
    elif opcion == OPCION_CANCELAR:
        ocupadas, recaudacion = ejecutar_cancelacion(
            ocupadas, recaudacion
        )
    elif opcion == OPCION_DISPONIBILIDAD:
        consultar_disponibilidad(ocupadas)
    elif opcion == OPCION_RECAUDACION:
        consultar_recaudacion(recaudacion)

    return ocupadas, recaudacion

# PROGRAMA PRINCIPAL


def main() -> None:
    """Ejecuta el menú principal de la aplicación.

    Returns:
        None: Esta función coordina el programa y no devuelve ningún valor.
    """
    ocupadas: int = 0
    recaudacion: float = 0.0
    opcion: str = ""

    while opcion != OPCION_SALIR:
        mostrar_menu()
        opcion = pedir_opcion()
        limpiar_pantalla()

        if opcion in OPCIONES_VALIDAS:
            try:
                ocupadas, recaudacion = procesar_opcion(
                    opcion, ocupadas, recaudacion
                )
            except ValueError as error:
                print(f"Error: {error}")
        elif opcion != OPCION_SALIR:
            print("Opción incorrecta.")

        if opcion != OPCION_SALIR:
            pausar_pantalla()
            limpiar_pantalla()

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()
