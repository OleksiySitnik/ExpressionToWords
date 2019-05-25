#!/usr/bin/python3.6
from expression_to_words.expression_ import Expression

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Сonverts a numerical expression into a words')
    parser.add_argument("-l", "--logicvalid", action="store_true")
    args = parser.parse_args()

    expression = input('Enter expression: ')
    e = Expression(expression)

    if args.logicvalid:
        if e.logically_valid():
            e.convert_to_words()
        else:
            print('invalid input')

    else:
        e.convert_to_words()
