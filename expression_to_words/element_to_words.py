from .symbols_to_word import PARTS_OF_NUMBER, OPERATIONS


class ElementToWords:

    def __init__(self, element):
        self.element = element
        self._words = []

    def _convert_operation_to_word(self):
        operations_and_braces = OPERATIONS

        return operations_and_braces[self.element]

    def _convert_num_to_words(self):
        int_element = abs(int(self.element))

        if int_element == 0:
            return 'zero'

        less_number = 0
        for elem in PARTS_OF_NUMBER:
            if int_element >= elem:
                less_number = elem
                continue

            div, mod = divmod(int_element, less_number)

            if div != 1:
                self.element = div
                self._convert_num_to_words()

            if int_element >= 100 and div == 1:
                self._words.append(PARTS_OF_NUMBER[1])
                self._words.append(PARTS_OF_NUMBER[less_number][:-1])

            else:
                self._words.append(PARTS_OF_NUMBER[less_number])

            if mod != 0:
                self.element = mod
                self._convert_num_to_words()

            return ' '.join(self._words)

    def convert_to_words(self):

        if self.element in OPERATIONS:
            return self._convert_operation_to_word()

        else:
            if self.element[0] == '-' and self.element[1:] != '0':
                return 'minus ' + self._convert_num_to_words()
            return self._convert_num_to_words()
