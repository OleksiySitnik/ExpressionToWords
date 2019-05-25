import pytest
from expression_to_words.expression_ import Expression

expressions = [
    "- 14 - 15 = - 29",
    "14* 2= 28",
    "18/2 =  10 - 1",
    "25 - 1 - 2 = 0",
    "2344 / 2=18 * 10 -1",
    "25-1 = 24",
    "- 1 + 15=- 14",
    " 18 * 2 - 2 = 29 - 1 * 13"
]

expected_parse_expressions = [
    ['-14', '-', '15', '=', '-29'],
    ['14', '*', '2', '=', '28'],
    ['18', '/', '2', '=', '10', '-', '1'],
    ['25', '-', '1', '-', '2', '=', '0'],
    ['2344', '/', '2', '=', '18', '*', '10', '-', '1'],
    ['25', '-', '1', '=', '24'],
    ['-1', '+', '15', '=', '-14']
]


@pytest.mark.parametrize("expression, expected", [
    (expressions[i], expected_parse_expressions[i]) for i in range(7)
])
def test_parse_expression(expression, expected):
    assert Expression(expression)._parse_expression() == expected


expected_converted_expressions = [
    "minus fourteen MINUS fifteen EQUALS minus twenty nine\n",
    "fourteen MULTIPLY BY two EQUALS twenty eight\n",
    "eighteen DIVIDED INTO two EQUALS ten MINUS one\n",
    "twenty five MINUS one MINUS two EQUALS zero\n",
    "two thousands three hundreds forty four DIVIDED INTO two EQUALS eighteen MULTIPLY BY ten MINUS one\n",
    "twenty five MINUS one EQUALS twenty four\n",
    "minus one PLUS fifteen EQUALS minus fourteen\n"
]


@pytest.mark.parametrize("expression, expected", [
    (expressions[i], expected_converted_expressions[i]) for i in range(7)
])
def test_convert_to_words(expression, expected, capsys):
    Expression(expression).convert_to_words()
    captured = capsys.readouterr()

    assert captured.out == f"Result: {expected}"
