import re
from collections import deque

from .element_to_words import ElementToWords
from .symbols_to_word import OPERATIONS, get_priority


class Expression:
    def __init__(self, expression_string):
        self.expression = expression_string

    def _parse_expression(self):

        if re.search(r"\d +\d", self.expression): # looking for parts of the expression
            raise SyntaxError                     # similar to '1 4', '23   1' ...

        result = []
        temp_str = ''

        for ch in self.expression:

            is_unary_minus = ch == '-' and \
                             (not result or result[-1] == '=') and \
                             (not temp_str or not temp_str[-1].isdigit())

            if ch.isdigit() or is_unary_minus:
                temp_str += ch

            elif ch in OPERATIONS:
                if temp_str:
                    result.append(temp_str)
                    temp_str = ''
                result.append(ch)

            elif not ch.isspace():
                raise SyntaxError

        if temp_str:
            result.append(temp_str)

        return result

    def convert_to_words(self):
        if not self.syntax_valid():
            print("invalid input")
            return

        result_list = []

        for elem in self._parse_expression():
            element = ElementToWords(elem)
            result_list.append(element.convert_to_words())

        result = " ".join(result_list)
        print(f"Result: {result}")

    def syntax_valid(self):
        try:
            expression_list = self._parse_expression()

        except SyntaxError:
            return False

        for i in range(len(expression_list)):
            if i % 2 == 0 and expression_list[i] in OPERATIONS or \
                    i % 2 == 1 and expression_list[i] not in OPERATIONS:
                return False

        return True if expression_list[-1] not in OPERATIONS else False

    def logically_valid(self):
        try:
            left_part, right_part = map(
                lambda e: Expression(e),
                self.expression.split('=')
            )
        except ValueError:
            return False

        if not left_part.syntax_valid() or not right_part.syntax_valid():
            return False

        if left_part.result() == right_part.result():
            return True

        return False

    def _shunting_yard(self):
        """Convert expression to reverse polish notation.

        >>> Expression("1 - 4 * 12 / 554")._shunting_yard()
        deque(['1', '4', '12', '*', '554', '/', '-'])

        >>> Expression("1 - 1 * 14 + 2 / 18")._shunting_yard()
        deque(['1', '1', '14', '*', '-', '2', '18', '/', '+'])

        """
        output_values = deque()
        stack_operators = deque()

        for element in self._parse_expression():

            if element in OPERATIONS:
                while (len(stack_operators) and
                       get_priority(stack_operators[-1]) >= get_priority(element)):
                    output_values.append(stack_operators.pop())

                stack_operators.append(element)

            else:
                output_values.append(element)

        while len(stack_operators) != 0:
            output_values.append(stack_operators.pop())

        return output_values

    def result(self):
        """Finds the result of the expression
        using reverse polish notation

        >>> Expression("14 + 14 / 2").result()
        21.0

        >>> Expression("-1 + 1 * 12 - 4").result()
        7.0
        """
        result = 0
        numbers = deque()
        for element in self._shunting_yard():
            if element in OPERATIONS:
                number1 = numbers.pop()
                number2 = numbers.pop()

                if element == "+":
                    result = number2 + number1

                elif element == "-":
                    result = number2 - number1

                elif element == "*":
                    result = number2 * number1

                elif element == "/":
                    result = number2 / number1

                numbers.append(result)
            else:
                numbers.append(float(element))

        return numbers.pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod()