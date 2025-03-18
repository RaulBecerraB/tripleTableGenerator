# Triple Table Generator

A Python program that parses mathematical expressions and generates a table of triples (triplos), which represents the expression broken down into elementary operations.

## Description

This program takes a mathematical expression as input (such as `x = (a * b) - c/d`) and breaks it down into a series of elementary operations, represented as triples. Each triple consists of:

- An operation (OP)
- Two operands (OPE1 and OPE2)
- A temporary variable (T) to store the result

The program follows operator precedence rules:

1. Parentheses are evaluated first
2. Multiplication and division are evaluated next
3. Addition and subtraction are evaluated last
4. Assignment is evaluated last

## Project Structure

The project is organized into several modules with specific responsibilities:

- `triple_generator.py`: Contains the `TripleTableGenerator` class which parses expressions and generates triples
- `table_formatter.py`: Contains the `TableFormatter` class for formatting the table output
- `cli.py`: Provides the command-line interface
- `app.py`: The main entry point for the application
- `utils.py`: Contains utility functions for expression processing
- `regex_patterns.py`: Contains all regular expression patterns used for parsing expressions
- `test_triple_generator.py`: Unit tests for the triple generator

## Example

For the input expression: `x = (a * b) - c/d`

The program generates the following triple table:

```
| T    | OP  | OPE1 | OPE2 |
| ---- | --- | ---- | ---- |
| T(0) | *   | a    | b    |
| T(1) | /   | c    | d    |
| T(2) | -   | T(0) | T(1) |
| T(3) | =   | x    | T(2) |
```

## How to Run

1. Make sure you have Python installed on your system.
2. Run the program using:
   ```
   python app.py
   ```
3. Enter a mathematical expression when prompted.
4. The program will display the triple table.
5. You can enter multiple expressions or type 'exit' to quit.

## Running Tests

To run the unit tests, use:

```
python test_triple_generator.py
```

## Supported Operations

- Assignment (=)
- Addition (+)
- Subtraction (-)
- Multiplication (\*)
- Division (/)
- Parentheses for grouping expressions

## Technical Details

The program uses a recursive descent parser approach to break down the expression according to operator precedence. It processes expressions from highest to lowest precedence, creating temporary variables to store intermediate results.
