# Regex patterns for expression parsing

# Pattern to match the innermost parenthesized expression
INNERMOST_PARENTHESES = r'\(([^()]*)\)'

# Pattern to match multiplication and division operations
MULTIPLICATIVE_OPERATORS = r'([a-zA-Z0-9()]+)\s*([*/])\s*([a-zA-Z0-9()]+)'

# Pattern to match addition and subtraction operations
ADDITIVE_OPERATORS = r'([a-zA-Z0-9()]+)\s*([+-])\s*([a-zA-Z0-9()]+)'

# Pattern to identify if a string is a temporary variable (T)
TEMP_VARIABLE = r'^T\(\d+\)$' 