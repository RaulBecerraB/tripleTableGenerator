from utils import process_parentheses, process_multiplicative_operators, process_additive_operators

class TripleTableGenerator:
    def __init__(self):
        self.triples = []
        self.temp_counter = 0
        
    def reset(self):
        self.triples = []
        self.temp_counter = 0
    
    def add_triple(self, op, ope1, ope2):
        """Add a new triple to the table"""
        triple = {
            'T': f'T({self.temp_counter})',
            'OP': op,
            'OPE1': ope1,
            'OPE2': ope2
        }
        self.triples.append(triple)
        result = triple['T']
        self.temp_counter += 1
        return result
    
    def parse_expression(self, expression):
        """Parse the expression and generate triples"""
        self.reset()
        
        # Handle assignment operations
        if '=' in expression:
            left, right = expression.split('=', 1)
            left = left.strip()
            right = right.strip()
            
            # Process the right side of the equation
            result = self.parse_subexpression(right)
            
            # Add the assignment triple
            self.add_triple('=', left, result)
            
        else:
            # If there's no assignment, just process the expression
            self.parse_subexpression(expression)
            
        return self.triples
    
    def parse_subexpression(self, expr):
        """Parse a subexpression recursively"""
        expr = expr.strip()
        
        # Process the expression using utility functions
        # First, process parenthesized expressions
        expr = process_parentheses(expr, self.parse_subexpression, self.add_triple)
        
        # Then, process multiplication and division
        expr = process_multiplicative_operators(expr, self.add_triple)
        
        # Finally, process addition and subtraction
        expr = process_additive_operators(expr, self.add_triple)
        
        return expr 