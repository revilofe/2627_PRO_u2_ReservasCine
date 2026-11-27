# RA3 — Reservas de cine

## Objetivo

Completa el programa de reservas de cine que encontrarás en `src/main.py`.
Durante la actividad practicarás estructuras de selección y repetición,
excepciones, programación estructurada, depuración, documentación y
aserciones.

El programa simula la gestión básica de las reservas de un cine. Permite
reservar y cancelar entradas, consultar la disponibilidad, calcular la
recaudación y procesar solicitudes de reserva.

La actividad se organiza en nueve ejercicios, uno por cada criterio RA3.a–RA3.i.
La secuencia recomendada es la que aparece en este documento. Al final, todas
las respuestas de código deben estar en `src/main.py`.

## Archivos de la plantilla

- `src/main.py`: punto de partida corregido que se entrega el día del examen.
  Implementa aquí todas las respuestas de RA3.a a RA3.e y RA3.g a RA3.i.
- `src/main-alum.py`: versión de práctica con errores para trabajar antes del
  examen. No la uses como sustituta de `src/main.py` durante el examen.
- `src/tabla.md`: tabla y respuestas escritas de RA3.f.
- `README_PAPEL.md`: versión para resolver los ejercicios en papel. No incluye
  RA3.e, porque ese ejercicio consiste en integrar el programa ejecutable.

Puedes ejecutar el programa desde la raíz con:

```bash
python3 src/main.py
```

No cambies las firmas indicadas en los ejercicios. Las funciones de
procesamiento deben recibir datos y devolver resultados; no deben utilizar
`input()` ni `print()`, salvo que el enunciado indique que son funciones de
presentación o de coordinación.

## Secuencia de ejercicios

### RA3.a — Mensaje de disponibilidad

Define la función:

```python
def obtener_mensaje_disponibilidad(disponibles: int) -> int:
    ...
```

La función recibe el número de entradas disponibles y devuelve la posición
correspondiente dentro de esta tupla, que debe estar definida en el módulo y en
este orden:

```python
MENSAJES_DISPONIBILIDAD: tuple[str, ...] = (
    "Aforo completo",
    "Últimas entradas disponibles",
    "Quedan pocas entradas",
    "Disponibilidad normal",
)
```

Las posiciones son:

- `0` si `disponibles == 0`.
- `1` si `disponibles < 5`.
- `2` si `disponibles < 15`.
- `3` en cualquier otro caso.

Ejemplos:

```python
obtener_mensaje_disponibilidad(0)  # 0
obtener_mensaje_disponibilidad(3)  # 1
```

Utiliza una estructura de selección. Esta función solo calcula y devuelve la
posición; no muestra el mensaje.

### RA3.b — Series completas vendidas

Define la función:

```python
def obtener_series_completas(
    ocupadas: int,
    aforo: int
) -> list[str]:
    ...
```

Define también una tupla con las series disponibles, en orden, desde `A` hasta
`L`. Cada serie representa diez entradas:

- `A` corresponde a `00–09`.
- `B` corresponde a `10–19`.
- Las siguientes series continúan del mismo modo.
- `L` corresponde a `110–119`.

La función debe construir y devolver una lista con las series cuyas diez
entradas estén vendidas. El identificador de una serie completa termina en
`00`: por ejemplo, `A00`, `B00` o `L00`.

Ejemplos:

```python
obtener_series_completas(55, 120)
# ["A00", "B00", "C00", "D00", "E00"]

obtener_series_completas(0, 120)
# []
```

Debe utilizar una estructura de repetición y limitarse a las series que caben
en el `aforo`. La función procesa datos y no muestra nada por consola.

### RA3.h — Crear una excepción propia

Crea la excepción `ReferenciaSerieError`, que se produce cuando una referencia
de serie no es válida.

Debe derivar de `ValueError` y su docstring debe explicar que se utiliza para
referencias de serie no válidas. En este ejercicio solo se crea la clase; su
uso se realizará en RA3.d.

### RA3.d — Validar una referencia de serie

Define:

```python
def crear_referencia(entrada: str) -> str:
    ...
```

Una referencia válida tiene una letra de serie entre `A` y `L` y un número de
entrada entre `0` y `9`. La función debe:

1. eliminar los espacios exteriores;
2. convertir la serie a mayúsculas;
3. validar la serie y el número;
4. devolver el número con dos dígitos.

Ejemplos:

```python
crear_referencia("A7")    # "A07"
crear_referencia(" l9 ")  # "L09"
crear_referencia("B03")   # "B03"
```

Si no se puede separar una serie y un número, lanza `ReferenciaSerieError`
con este mensaje exacto:

```text
La referencia no tiene un formato válido.
```

Si la serie no está entre `A` y `L`, o el número no está entre `0` y `9`,
lanza `ReferenciaSerieError` con este mensaje exacto:

```text
La serie debe estar entre A y L y el número entre 0 y 9.
```

Deben producir una excepción `""`, `"ABC"`, `"M03"`, `"A10"` y `"A-1"`. La
función no debe utilizar `input()` ni `print()` y debe tener un único `return`
al final. Usa control de excepciones para detectar errores y lanza la excepción
propia con el mensaje correspondiente.

### RA3.f — Tabla de seguimiento y depuración

La función `procesar_solicitudes_reserva()` ya está implementada. Debes seguir
su ejecución para entender cómo funciona.

```python
def procesar_solicitudes_reserva(
    solicitudes: tuple[int, ...],
    ocupadas: int,
    recaudacion: float,
    aforo: int,
    precio_entrada: float
) -> tuple[int, float]:
    """Procesa un lote de solicitudes de reserva."""
    indice: int = 0

    while True:
        if indice >= len(solicitudes):
            break

        cantidad: int = solicitudes[indice]
        indice += 1

        if cantidad == 0:
            break

        if cantidad < 0:
            continue

        disponibles: int = aforo - ocupadas

        if cantidad > disponibles:
            continue

        ocupadas += cantidad
        recaudacion += cantidad * precio_entrada

    return ocupadas, recaudacion
```

En `src/tabla.md`, completa la tabla de seguimiento suponiendo que llamas a la función con estos argumentos:

```python
solicitudes = (20, -1, 6, 3, 30, 4, 0, 1)
aforo = 60
ocupadas = 0
recaudacion = 0.0
precio_entrada = 7.50
```

La tabla debe incluir, para cada iteración ejecutada, los valores finales de
`indice`, `cantidad`, `disponibles`, `ocupadas` y `recaudacion`. Incluye
también el estado inicial y marca las iteraciones que ya no se ejecutan.

Después de la tabla, responde:

1. qué solicitudes se procesan correctamente;
2. qué solicitudes se ignoran y por qué;
3. qué solicitud finaliza el bucle;
4. qué valores finales devuelven `ocupadas` y `recaudacion`;
5. si el funcionamiento es correcto.


### RA3.i — Probar con aserciones

Crea en `src/main.py`:

```python
def test_procesar_solicitudes_reserva() -> None:
    ...
```

La función debe llamar a `procesar_solicitudes_reserva()` con:

```python
solicitudes = (20, -1, 6, 3, 30, 4, 0, 1)
aforo = 60
ocupadas = 0
recaudacion = 0.0
precio_entrada = 7.50
```

Debe utilizar `assert` para comprobar que el resultado es `(59, 442.50)`.
Si el resultado no coincide, la aserción debe producir `AssertionError` e
indicar el resultado esperado y el resultado real. La función de prueba no debe
pedir datos ni mostrar mensajes.

### RA3.c — Programación estructurada

Define o refactoriza la función `procesar_solicitudes_reserva()` con la siguiente firma:

```python
def procesar_solicitudes_reserva(
    solicitudes: tuple[int, ...],
    ocupadas: int,
    recaudacion: float,
    aforo: int,
    precio_entrada: float
) -> tuple[int, float]:
    ...
```

Debe conservar el comportamiento de la versión inicial.

La nueva versión debe cumplir los siguientes requisitos:
- no utiliza `while True`;
- no utiliza `break`;
- no utiliza `continue`;
- utiliza condiciones o variables centinela para controlar el bucle;
- tiene un único `return`, situado al final;
- no utiliza `input()` ni `print()`.

### RA3.g — Documentar y comentar el código

Documenta `procesar_solicitudes_reserva()` sin cambiar su comportamiento. El
docstring debe seguir el estilo Google e incluir:

- una descripción detallada;
- `Args` con el significado de todos los parámetros;
- `Returns` con el significado de la tupla devuelta.

La explicación debe indicar qué ocurre con `0`, con las cantidades negativas,
con las cantidades positivas y con las solicitudes que superan la
disponibilidad. Añade comentarios junto a las decisiones del algoritmo que
expliquen esas situaciones.

### RA3.e — Integrar las funciones en el programa

Este ejercicio se realiza sobre el programa completo y evalúa conjuntamente la
integración de RA3.a y RA3.b.

#### Integrar la disponibilidad

En `consultar_disponibilidad(ocupadas)`, después de calcular
`disponibles`:

1. llama a `obtener_mensaje_disponibilidad(disponibles)`;
2. guarda la posición devuelta;
3. utiliza esa posición sobre `MENSAJES_DISPONIBILIDAD`;
4. muestra el mensaje correspondiente.

`obtener_mensaje_disponibilidad()` decide la posición y
`consultar_disponibilidad()` coordina y presenta la consulta.

#### Integrar las series completas

Añade al menú:

```text
5. Consultar series completas
```

Para esta opción:

1. crea, por ejemplo, `OPCION_SERIES_COMPLETAS = "5"`;
2. incluye la constante en `OPCIONES_VALIDAS`;
3. muestra la opción en `mostrar_menu()`;
4. crea `consultar_series_completas(ocupadas, aforo)`;
5. llama desde ella a `obtener_series_completas(ocupadas, aforo)`;
6. pasa la lista a `mostrar_series_completas()`;
7. conecta la opción desde `procesar_opcion()`.

La función `mostrar_series_completas(series)` debe mostrar una serie por línea
si la lista no está vacía y, si está vacía, exactamente:

```text
No hay series completas vendidas.
```

La estructura de llamadas esperada es:

```text
main()
└── procesar_opcion()
    └── consultar_series_completas()
        ├── obtener_series_completas()
        └── mostrar_series_completas()
```

Mantén separadas estas responsabilidades:

- procesamiento: recibe datos y devuelve resultados;
- coordinación: conecta el menú con el procesamiento;
- presentación: muestra los resultados;
- `procesar_opcion()`: decide qué operación se ejecuta.

No dupliques dentro de las funciones de coordinación los algoritmos de
`obtener_mensaje_disponibilidad()` ni `obtener_series_completas()`.

## Puntuación

Cada ejercicio vale 10 puntos. Las evidencias se valoran por separado:

| Criterio | Desglose de evidencias | Máximo |
|---|---|---:|
| RA3.a | Tupla 2 + casos límite 4 + selección 2 + contrato sin E/S 2 | 10 |
| RA3.b | Series 2 + casos 4 + repetición 2 + contrato sin E/S 2 | 10 |
| RA3.c | Comportamiento 4 + sin saltos 3 + retorno final 2 + sin E/S 1 | 10 |
| RA3.d | Normalización 3 + formato 3 + valores 3 + contrato 1 | 10 |
| RA3.e | Disponibilidad 3 + menú 2 + presentación 2 + coordinación 2 + despacho 1 | 10 |
| RA3.f | Iteraciones 1–4: 3 + iteraciones 5–9: 3 + respuestas 2 + conclusión 2 | 10 |
| RA3.g | Docstring Google 4 + explicación 3 + comentarios 3 | 10 |
| RA3.h | Herencia 5 + docstring 5 | 10 |
| RA3.i | Función 3 + datos 3 + aserción 3 + sin E/S 1 | 10 |
| **Total** |  | **90** |

La fila inicial de `src/tabla.md` ya está dada y no aporta puntos por sí sola.
Los niveles automáticos por criterio son: **0**, sin evidencia; **1–2**,
inicial; **3–5**, en desarrollo; **6–8**, adecuado; **9**, casi completo; y
**10**, completo. Por tanto, la máxima puntuación solo se alcanza con todas las
evidencias del criterio. Antes de entregar, comprueba que `src/main.py` se puede
importar y ejecutar y que `src/tabla.md` contiene todas las respuestas.
