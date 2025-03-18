import re
from regex_patterns import (
    PARENTESIS_INTERNOS,
    OPERADORES_MULTIPLICATIVOS,
    OPERADORES_ADITIVOS,
    VARIABLE_TEMPORAL
)

def procesar_parentesis(expr, funcion_analisis, funcion_agregar_triplo):
    """
    Procesa expresiones entre paréntesis en una expresión dada
    
    Args:
        expr: La expresión a procesar
        funcion_analisis: Una función callback para analizar subexpresiones
        funcion_agregar_triplo: Una función callback para agregar triplos
        
    Returns:
        La expresión procesada con los paréntesis resueltos
    """
    expr = expr.strip()
    
    # Manejar primero las expresiones entre paréntesis
    if '(' in expr and not expr.startswith('T('):
        # Encontrar los paréntesis más internos
        while '(' in expr and not expr.startswith('T('):
            # Buscar la expresión entre paréntesis más interna
            mas_interno = re.search(PARENTESIS_INTERNOS, expr)
            if not mas_interno:
                break
            
            # Asegurarse de que no estamos coincidiendo con un patrón T(n)
            coincidencia_completa = mas_interno.group(0)
            if coincidencia_completa.startswith('T(') and coincidencia_completa.endswith(')'):
                # Este es un patrón T(n), omitirlo
                inicio_coincidencia = mas_interno.start()
                expr = expr[:inicio_coincidencia] + "MARCADOR_TEMPORAL" + expr[mas_interno.end():]
                expr = expr.replace("MARCADOR_TEMPORAL", coincidencia_completa)
                continue
            
            # Procesar la expresión interna
            expr_interna = mas_interno.group(1)
            resultado = funcion_analisis(expr_interna)
            
            # Reemplazar la expresión entre paréntesis con su resultado
            expr = expr.replace(f'({expr_interna})', resultado)
    
    return expr

def procesar_operadores_multiplicativos(expr, funcion_agregar_triplo):
    """
    Procesa operaciones de multiplicación y división en una expresión
    
    Args:
        expr: La expresión a procesar
        funcion_agregar_triplo: Una función callback para agregar triplos
        
    Returns:
        La expresión procesada con las operaciones multiplicativas resueltas
    """
    # Procesar multiplicación y división
    while '*' in expr or '/' in expr:
        coincidencia_md = re.search(OPERADORES_MULTIPLICATIVOS, expr)
        if not coincidencia_md:
            break
            
        ope1 = coincidencia_md.group(1)
        op = coincidencia_md.group(2)
        ope2 = coincidencia_md.group(3)
        
        resultado = funcion_agregar_triplo(op, ope1, ope2)
        
        # Reemplazar la expresión coincidente con el resultado
        coincidencia_completa = coincidencia_md.group(0)
        expr = expr.replace(coincidencia_completa, resultado, 1)
    
    return expr

def procesar_operadores_aditivos(expr, funcion_agregar_triplo):
    """
    Procesa operaciones de suma y resta en una expresión
    
    Args:
        expr: La expresión a procesar
        funcion_agregar_triplo: Una función callback para agregar triplos
        
    Returns:
        La expresión procesada con las operaciones aditivas resueltas
    """
    # Procesar suma y resta
    while '+' in expr or '-' in expr:
        coincidencia_sr = re.search(OPERADORES_ADITIVOS, expr)
        if not coincidencia_sr:
            break
            
        ope1 = coincidencia_sr.group(1)
        op = coincidencia_sr.group(2)
        ope2 = coincidencia_sr.group(3)
        
        resultado = funcion_agregar_triplo(op, ope1, ope2)
        
        # Reemplazar la expresión coincidente con el resultado
        coincidencia_completa = coincidencia_sr.group(0)
        expr = expr.replace(coincidencia_completa, resultado, 1)
    
    return expr 