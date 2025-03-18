from triple_generator import GeneradorTablaTriplos
from table_formatter import FormateadorTabla

class CLI:
    def __init__(self):
        self.generador = GeneradorTablaTriplos()
        
    def ejecutar(self):
        """
        Ejecuta la interfaz de línea de comandos para el generador de tabla de triplos
        """
        print("Generador de Tabla de Triplos")
        print("============================")
        print("Ingrese una expresión matemática (por ejemplo, 'x = (a * b) - c/d'):")
        
        while True:
            expresion = input("> ")
            if not expresion or expresion.lower() in ('salir', 'exit', 'quit'):
                break
                
            triplos = self.generador.analizar_expresion(expresion)
            tabla_formateada = FormateadorTabla.formatear_tabla_triplos(triplos)
            
            print("\nTabla de Triplos Generada:")
            print(tabla_formateada)
            print("\nIngrese otra expresión o 'salir' para terminar:")


def main():
    cli = CLI()
    cli.ejecutar()


if __name__ == "__main__":
    main() 