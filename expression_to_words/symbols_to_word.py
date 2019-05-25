PARTS_OF_NUMBER = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundreds',
        10 ** 3: 'thousands',
        10 ** 6: 'millions',
        10 ** 9: 'billions',
    }

OPERATIONS = {
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MULTIPLY BY',
    '/': 'DIVIDED INTO',
    '=': 'EQUALS'
}


def get_priority(c):
    priorities = {'+': 1, '-': 1, '*': 2, '/': 2}
    return priorities.get(c, 0)
