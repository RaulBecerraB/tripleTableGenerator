from triple_generator import TripleTableGenerator
from table_formatter import TableFormatter

class CLI:
    def __init__(self):
        self.generator = TripleTableGenerator()
        
    def run(self):
        """
        Run the command line interface for the triple table generator
        """
        print("Triple Table Generator")
        print("=====================")
        print("Enter a mathematical expression (e.g., 'x = (a * b) - c/d'):")
        
        while True:
            expression = input("> ")
            if not expression or expression.lower() in ('exit', 'quit'):
                break
                
            triples = self.generator.parse_expression(expression)
            formatted_table = TableFormatter.format_triple_table(triples)
            
            print("\nGenerated Triple Table:")
            print(formatted_table)
            print("\nEnter another expression or 'exit' to quit:")


def main():
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main() 