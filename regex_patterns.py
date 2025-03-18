# Patrones de expresiones regulares para el análisis de expresiones

# Patrón para encontrar la expresión entre paréntesis más interna
PARENTESIS_INTERNOS = r'\(([^()]*)\)'

# Patrón para encontrar operaciones de multiplicación y división
OPERADORES_MULTIPLICATIVOS = r'([a-zA-Z0-9()]+)\s*([*/])\s*([a-zA-Z0-9()]+)'

# Patrón para encontrar operaciones de suma y resta
OPERADORES_ADITIVOS = r'([a-zA-Z0-9()]+)\s*([+-])\s*([a-zA-Z0-9()]+)'

# Patrón para identificar si una cadena es una variable temporal (T)
VARIABLE_TEMPORAL = r'^T\(\d+\)$' 