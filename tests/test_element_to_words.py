import pytest

from expression_to_words.element_to_words import ElementToWords

elements = [
    "123", "-345012", "0", "435312", "12",
    "-", "+", "/", "*", "=", "1", "7"
]

expected_converted_elements = [
    "one hundred twenty three",
    "minus three hundreds forty five thousands twelve",
    "zero",
    "four hundreds thirty five thousands three hundreds twelve",
    "twelve",
    "MINUS",
    "PLUS",
    "DIVIDED INTO",
    "MULTIPLY BY",
    "EQUALS",
    "one",
    "seven"
]

@pytest.mark.parametrize("element, expected", [
    (elements[i], expected_converted_elements[i]) for i in range(7)
])
def test_parse_expression(element, expected):
    assert ElementToWords(element).convert_to_words() == expected