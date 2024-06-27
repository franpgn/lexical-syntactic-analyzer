# LISP to Postfix Converter

This project converts LISP expressions to postfix notation using a lexer and parser implemented with the PLY (Python Lex-Yacc) library.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Tests](#tests)
- [License](#license)
- [References](#references)

## Introduction

This project implements a lexer and parser to convert LISP-like expressions into postfix notation. It is designed to handle basic arithmetic operations with nested expressions.

## Features

- Parses LISP expressions and converts them to postfix notation.
- Supports the following operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Handles nested expressions and ensures correct operator precedence.

## Prerequisites

- Python 3.x
- PLY library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/franpgn/lexical-syntactic-analyzer.git
    cd lexical-syntatic-analyzer
    ```

2. Install the PLY library:
    ```sh
    pip install ply
    ```

## Usage

1. Run the main application:
    ```sh
    python src/app.py
    ```

2. Enter LISP expressions to convert them to postfix notation. For example:
    ```plaintext
    LISP > (* z (+ x y))
    Postfix: x y + z *
    ```

## File Structure

- `src/lexer.py`: Defines the lexer which tokenizes the input LISP expressions.
- `src/parser.py`: Defines the parser which parses the tokenized input and converts it to postfix notation.
- `src/app.py`: Main application file that takes user input and processes it using the lexer and parser.
- `tests/test_lexer.py`: Contains tests for the lexer.
- `tests/test_parser.py`: Contains tests for the parser.

### Lexer (`src/lexer.py`)

The lexer defines tokens for identifiers, numbers, and operators. It also handles whitespace and errors.

### Parser (`src/parser.py`)

The parser defines grammar rules to convert LISP expressions into postfix notation. It uses the lexer tokens to parse the input and generate the correct postfix expression.

### Main Application (`src/app.py`)

The main application file takes user input, processes it through the parser, and prints the postfix notation.

### Tests (`tests/test_lexer.py` and `tests/test_parser.py`)

The test files contain unit tests to verify the functionality of the lexer and parser. They ensure that the components behave as expected and handle edge cases.

## Tests

To run the tests, use the following commands:

1. Test the lexer:
    ```sh
    python -m unittest tests/test_lexer.py
    ```

2. Test the parser:
    ```sh
    python -m unittest tests/test_parser.py
    ```

These tests ensure that the lexer and parser are functioning correctly and can handle various LISP expressions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## References

- [PLY Documentation](https://github.com/dabeaz/ply/blob/master/doc/ply.md)
- [PLY GitHub Repository](https://github.com/dabeaz/ply?tab=readme-ov-file)
