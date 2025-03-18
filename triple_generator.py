from utils import procesar_parentesis, procesar_operadores_multiplicativos, procesar_operadores_aditivos

class GeneradorTablaTriplos:
    def __init__(self):
        self.triplos = []
        self.contador_temp = 0
        
    def reiniciar(self):
        self.triplos = []
        self.contador_temp = 0
    
    def agregar_triplo(self, op, ope1, ope2):
        """Agregar un nuevo triplo a la tabla"""
        triplo = {
            'T': f'T({self.contador_temp})',
            'OP': op,
            'OPE1': ope1,
            'OPE2': ope2
        }
        self.triplos.append(triplo)
        resultado = triplo['T']
        self.contador_temp += 1
        return resultado
    
    def analizar_expresion(self, expresion):
        """Analizar la expresión y generar triplos"""
        self.reiniciar()
        
        # Manejar operaciones de asignación
        if '=' in expresion:
            izquierda, derecha = expresion.split('=', 1)
            izquierda = izquierda.strip()
            derecha = derecha.strip()
            
            # Procesar el lado derecho de la ecuación
            resultado = self.analizar_subexpresion(derecha)
            
            # Agregar el triplo de asignación
            self.agregar_triplo('=', izquierda, resultado)
            
        else:
            # Si no hay asignación, simplemente procesar la expresión
            self.analizar_subexpresion(expresion)
            
        return self.triplos
    
    def analizar_subexpresion(self, expr):
        """Analizar una subexpresión recursivamente"""
        expr = expr.strip()
        
        # Procesar la expresión utilizando funciones de utilidad
        # Primero, procesar expresiones entre paréntesis
        expr = procesar_parentesis(expr, self.analizar_subexpresion, self.agregar_triplo)
        
        # Luego, procesar multiplicación y división
        expr = procesar_operadores_multiplicativos(expr, self.agregar_triplo)
        
        # Finalmente, procesar suma y resta
        expr = procesar_operadores_aditivos(expr, self.agregar_triplo)
        
        return expr 