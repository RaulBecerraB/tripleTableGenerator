# Generador de Tabla de Triplos

Un programa en Python que analiza expresiones matemáticas y genera una tabla de triplos, que representa la expresión desglosada en operaciones elementales.

## Descripción

Este programa toma una expresión matemática como entrada (como `x = (a * b) - c/d`) y la descompone en una serie de operaciones elementales, representadas como triplos. Cada triplo consta de:

- Una operación (OP)
- Dos operandos (OPE1 y OPE2)
- Una variable temporal (T) para almacenar el resultado

El programa sigue las reglas de precedencia de operadores:

1. Los paréntesis se evalúan primero
2. La multiplicación y división se evalúan después
3. La suma y resta se evalúan a continuación
4. La asignación se evalúa al final

## Estructura del Proyecto

El proyecto está organizado en varios módulos con responsabilidades específicas:

- `triple_generator.py`: Contiene la clase `GeneradorTablaTriplos` que analiza expresiones y genera triplos
- `table_formatter.py`: Contiene la clase `FormateadorTabla` para dar formato a la salida de la tabla
- `cli.py`: Proporciona la interfaz de línea de comandos
- `app.py`: El punto de entrada principal para la aplicación
- `utils.py`: Contiene funciones de utilidad para el procesamiento de expresiones
- `regex_patterns.py`: Contiene todos los patrones de expresiones regulares utilizados para analizar expresiones
- `test_triple_generator.py`: Pruebas unitarias para el generador de triplos

## Ejemplo

Para la expresión de entrada: `x = (a * b) - c/d`

El programa genera la siguiente tabla de triplos:

```
| T    | OP  | OPE1 | OPE2 |
| ---- | --- | ---- | ---- |
| T(0) | *   | a    | b    |
| T(1) | /   | c    | d    |
| T(2) | -   | T(0) | T(1) |
| T(3) | =   | x    | T(2) |
```

## Cómo Ejecutar

1. Asegúrese de tener Python instalado en su sistema.
2. Ejecute el programa usando:
   ```
   python app.py
   ```
3. Ingrese una expresión matemática cuando se le solicite.
4. El programa mostrará la tabla de triplos.
5. Puede ingresar múltiples expresiones o escribir 'salir' para terminar.

## Ejecutando Pruebas

Para ejecutar las pruebas unitarias, use:

```
python test_triple_generator.py
```

## Operaciones Soportadas

- Asignación (=)
- Suma (+)
- Resta (-)
- Multiplicación (\*)
- División (/)
- Paréntesis para agrupar expresiones

## Detalles Técnicos

El programa utiliza un enfoque de análisis recursivo descendente para descomponer la expresión según la precedencia de operadores. Procesa las expresiones desde la precedencia más alta a la más baja, creando variables temporales para almacenar resultados intermedios.
