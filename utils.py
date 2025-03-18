import re
from regex_patterns import (
    INNERMOST_PARENTHESES,
    MULTIPLICATIVE_OPERATORS,
    ADDITIVE_OPERATORS,
    TEMP_VARIABLE
)

def process_parentheses(expr, parse_callback, add_triple_callback):
    """
    Process parenthesized expressions in a given expression
    
    Args:
        expr: The expression to process
        parse_callback: A callback function to parse subexpressions
        add_triple_callback: A callback function to add triples
        
    Returns:
        The processed expression with parentheses resolved
    """
    expr = expr.strip()
    
    # Handle parenthesized expressions first
    if '(' in expr and not expr.startswith('T('):
        # Find the innermost parentheses
        while '(' in expr and not expr.startswith('T('):
            # Match the innermost parenthesized expression
            innermost = re.search(INNERMOST_PARENTHESES, expr)
            if not innermost:
                break
            
            # Make sure we're not matching a T(n) pattern
            full_match = innermost.group(0)
            if full_match.startswith('T(') and full_match.endswith(')'):
                # This is a T(n) pattern, skip it
                match_start = innermost.start()
                expr = expr[:match_start] + "TEMP_PLACEHOLDER" + expr[innermost.end():]
                expr = expr.replace("TEMP_PLACEHOLDER", full_match)
                continue
            
            # Process the inner expression
            inner_expr = innermost.group(1)
            result = parse_callback(inner_expr)
            
            # Replace the parenthesized expression with its result
            expr = expr.replace(f'({inner_expr})', result)
    
    return expr

def process_multiplicative_operators(expr, add_triple_callback):
    """
    Process multiplication and division operations in an expression
    
    Args:
        expr: The expression to process
        add_triple_callback: A callback function to add triples
        
    Returns:
        The processed expression with multiplicative operations resolved
    """
    # Process multiplication and division
    while '*' in expr or '/' in expr:
        md_match = re.search(MULTIPLICATIVE_OPERATORS, expr)
        if not md_match:
            break
            
        ope1 = md_match.group(1)
        op = md_match.group(2)
        ope2 = md_match.group(3)
        
        result = add_triple_callback(op, ope1, ope2)
        
        # Replace the matched expression with the result
        full_match = md_match.group(0)
        expr = expr.replace(full_match, result, 1)
    
    return expr

def process_additive_operators(expr, add_triple_callback):
    """
    Process addition and subtraction operations in an expression
    
    Args:
        expr: The expression to process
        add_triple_callback: A callback function to add triples
        
    Returns:
        The processed expression with additive operations resolved
    """
    # Process addition and subtraction
    while '+' in expr or '-' in expr:
        as_match = re.search(ADDITIVE_OPERATORS, expr)
        if not as_match:
            break
            
        ope1 = as_match.group(1)
        op = as_match.group(2)
        ope2 = as_match.group(3)
        
        result = add_triple_callback(op, ope1, ope2)
        
        # Replace the matched expression with the result
        full_match = as_match.group(0)
        expr = expr.replace(full_match, result, 1)
    
    return expr 