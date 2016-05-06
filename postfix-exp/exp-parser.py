import unittest
from Stack import Stack

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
OPERATORS = '(+-*/^'

OP_PRECEDENCE = {
    '(': 1,
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
    '^': 4
}


def is_higher_or_same(op1, op2):
    return OP_PRECEDENCE[op1] >= OP_PRECEDENCE[op2]


def parse_to_postfix(exp):
    exp = list(exp)
    postfix = []
    operators = Stack()

    for symbol in exp:
        if symbol == ' ':
            continue
        elif symbol in ALPHABET:
            postfix.append(symbol)
        elif symbol is '(':
            operators.push(symbol)

        elif symbol in OPERATORS:
            while not operators.isEmpty() and is_higher_or_same(operators.peek(), symbol):
                postfix.append(operators.pop())

            operators.push(symbol)
        elif symbol == ')':
            if not operators.isEmpty():
                tmp_sym = operators.pop()
                while tmp_sym != '(':
                    postfix.append(tmp_sym)
                    if not operators.isEmpty():
                        tmp_sym = operators.pop()
                    else:
                        raise RuntimeError('couldn\'t match parentheses')

    while not operators.isEmpty():
        postfix.append(operators.pop())

    return ' '.join(postfix)


def apply_op(valueA, valueB, op):
    if op == '+':
        return valueA + valueB
    elif op == '-':
        return valueA - valueB
    elif op == '*':
        return valueA * valueB
    else:
        return valueA / valueB


def eval_postfix(exp):
    exp = exp.split()
    stack = Stack()

    for symbol in exp:
        if symbol in '0123456789':
            stack.push(int(symbol))
        else:
            valueB = stack.pop()
            valueA = stack.pop()
            stack.push(apply_op(valueA, valueB, symbol))

    return stack.pop()

# print('17 10 + 3 * 9 / = ', eval_postfix('17 10 + 3 * 9 /'))


class TestParser(unittest.TestCase):
    def test_parse_1(self):
        self.assertEqual(parse_to_postfix('A + B'), 'A B +')

    def test_parse_2(self):
        self.assertEqual(parse_to_postfix('A + B + C'), 'A B + C +')

    def test_parse_3(self):
        self.assertEqual(parse_to_postfix('A + B * C'), 'A B C * +')

    def test_parse_4(self):
        self.assertEqual(parse_to_postfix('A * B - C'), 'A B * C -')

    def test_parse_5(self):
        self.assertEqual(parse_to_postfix('A * B - C / D + E'), 'A B * C D / - E +')

    def test_parse_6(self):
        self.assertEqual(parse_to_postfix('( A + B ) * ( C + D )'), 'A B + C D + *')

    def test_parse_7(self):
        self.assertEqual(parse_to_postfix('( A + B ) * C'), 'A B + C *')

    def test_parse_8(self):
        self.assertEqual(parse_to_postfix('A + B * C'), 'A B C * +')

    def test_parse_9(self):
        self.assertEqual(parse_to_postfix('5 * 3 ^ (4 - 2)'), '5 3 4 2 - ^ *')


class TestEval(unittest.TestCase):
    def test_eval_1(self):
        self.assertEqual(eval_postfix('2 3 +'), 5)

    def test_eval_2(self):
        self.assertEqual(eval_postfix('7 8 + 3 2 + /'), 3)
