from collections import Counter
import operator
from sympy.ntheory import factorint, primerange
import re
import sys


class Program:
    @staticmethod
    def get_prime_factors(n):
        """
        :param n: primorial (product of some prime numbers)
        :return: prime factors in sorted order, maybe 0
        """
        plain_factors = factorint(n)
        max_prime = max(plain_factors.items(), key=operator.itemgetter(0))[0]
        for _prime in primerange(2, max_prime + 1):
            if _prime not in plain_factors:
                plain_factors[_prime] = 0

        factors = list(map(operator.itemgetter(1), sorted(plain_factors.items(), key=operator.itemgetter(0))))

        return factors

    @staticmethod
    def line_preprocess(i, line, plain=False):
        """
        This function gets a line of program and return all info about line.

        :param i: line number
        :param line: one line of program
        :returns: 3 element tuple (type,label,variables):
                   type: 0,1,2 or 3
                   label : label of line if exists otherwise empty string
                   variables: just one variable in case of addition and subtraction and (variable, label) in case of IF satement.
        :raises SyntaxError: if line doesn't match language
        """
        if line.islower():
            raise SyntaxError('Syntax Error in line %d. You should use UPPERCASE letters' % i)

        if re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*$', line):  # matches: [L] v <- v
            _vars = re.findall(r'(\w\d*)', line)  # finds variable names
            if len(_vars) == 2: _vars.insert(0, '')  # add empty label
            if _vars[1] != _vars[2]:
                raise SyntaxError('Syntax Error in line %d, Cant use v <- w' % i)
            _label = _vars[0]
            if plain:
                _var = _vars[1]
            else:
                _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[
                    1]  # convert X1 to python list syntax X[0]
            return 0, _label, _var

        elif re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*\s*\+\s*1$', line):  # matches [L] v <- v + 1
            _vars = re.findall(r'(\w\d*)', line)
            if len(_vars) == 3: _vars.insert(0, '')
            if _vars[1] != _vars[2]:
                raise SyntaxError('Syntax Error in line %d, Cant use v <- w + 1' % i)
            _label = _vars[0]
            if plain:
                _var = _vars[1]
            else:
                _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[1]
            return 1, _label, _var

        elif re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*\s*-\s*1$', line):  # matches [L] v <- v - 1
            _vars = re.findall(r'(\w\d*)', line)
            if len(_vars) == 3: _vars.insert(0, '')
            if _vars[1] != _vars[2]:
                raise SyntaxError('Syntax Error in line %d, Cant use v <- w - 1' % i)
            _label = _vars[0]
            if plain:
                _var = _vars[1]
            else:
                _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[1]
            return 2, _label, _var

        elif re.match('^(\[\w\d*\])?\s*IF\s*\w\d*\s*!=\s*0\s*GOTO\s*\w\d*$', line):  # matches [L] IF V != 0 GOTO L2
            _vars = re.findall(r'(\w\d*)', line)
            if _vars[0] == 'I':  # add empty label
                _vars.insert(0, '')

            _label = _vars[0]

            if plain:
                _var = _vars[3]
            else:
                _var = "%s[%d]" % (_vars[3][0], int(_vars[3][1:]) - 1) if _vars[3] != 'Y' else _vars[3]

            return 3, _label, _var, _vars[-1]
        else:  # Unknown line syntax
            raise SyntaxError('Syntax Error in line %d' % i)


class PAIRING:

    @staticmethod
    def unpair(n):
        """
        :param n: result of 2^x(2*y+1) - 1
        :return: x,y
        """
        n += 1
        x = 0
        while n % 2 == 0:
            x += 1
            n /= 2
        y = (n - 1) // 2
        return x, int(y)

    @staticmethod
    def pair(x, y):
        """

        :param x: int
        :param y: int
        :return: pairing of x, y
        """
        return 2 ** x * (2 * y + 1) - 1


class Label:
    labels = " ABCDE"

    @staticmethod
    def from_code(a):
        """

        :param a: 1,2,....
        :return: a label: A1,B1,...
        """
        _label = ''

        if a != 0:
            d, r = divmod(a - 1, 5)
            _label = Label.labels[r + 1] + str(d + 1)
        return _label

    @staticmethod
    def to_code(label):
        """

        :param label: a valid label name: A1,B1,..E1,A2,...
        :return: 1,2,3,...
        """

        _l, _n = label[0], label[1:]
        return Label.labels.index(_l) + (int(_n) - 1) * 5


class Variable:
    vars = " XZ"

    @staticmethod
    def from_code(c):
        """

        :param c: variable code 1,2,3,...
        :return: variable Y,X1,Z1,X2,Z2,...
        """
        _var = "Y"
        if c > 1:
            d, r = divmod(c - 2, 2)
            _var = Variable.vars[r + 1] + str(d + 1)
        return _var

    @staticmethod
    def to_code(var):
        """

        :param var: variable: Y,X1,Z1,X2,Z2,...
        :return:  variable code: 1,2,3,...
        """

        if var == "Y":
            return 1
        _l, _n = var[0], var[1:]
        return 1 + Variable.vars.index(_l) + (int(_n) - 1) * 2


class Instruction:
    @staticmethod
    def from_code(p):
        """

        :param p: p = <a,<b,c>>
        :return: equivalent instruction
        """
        a, t = PAIRING.unpair(p)
        b, c = PAIRING.unpair(t)
        _label = Label.from_code(a)
        _var = Variable.from_code(c + 1)

        if b == 0:
            if _label:
                instruction = "[{0}] {1} <- {1}".format(_label, _var)
            else:
                instruction = "{0} <- {0}".format(_var)
        elif b == 1:
            if _label:
                instruction = "[{0}] {1} <- {1} + 1".format(_label, _var)
            else:
                instruction = "{0} <- {0} + 1".format(_var)
        elif b == 2:
            if _label:
                instruction = "[{0}] {1} <- {1} - 1".format(_label, _var)
            else:
                instruction = "{0} <- {0} - 1".format(_var)
        else:
            b -= 2
            _label2 = Label.from_code(b)
            if _label:
                instruction = "[{0}] IF {1} != 0 GOTO {2}".format(_label, _var, _label2)
            else:
                instruction = "IF {0} != 0 GOTO {1}".format(_var, _label2)
        return instruction

    @staticmethod
    def to_code(line_info):
        """

        :param line_info: result of line_preprocessing function
        :return: <a,<b,c>>
        """
        _type, _label, *_vars = line_info
        a, b, c = [0] * 3
        if _label:
            a = Label.to_code(_label)

        c = Variable.to_code(_vars[0]) - 1
        if _type != 3:
            b = _type
        else:
            b = 2 + Label.to_code(_vars[1])
        return PAIRING.pair(a, PAIRING.pair(b, c))


def decode(x, factorize=True):
    """
    :param x: program code if factorize = True, else list of prime factors in sorted order
    :return: list of instructions
    """
    op_codes = []
    instructions = Program.get_prime_factors(x + 1) if factorize else x

    for instruction in instructions:
        op_codes.append(Instruction.from_code(instruction))
    return op_codes


def encode(file_name):
    """

    :param file_name:
    :return: list of prime factors
    """
    with open(file_name) as source:
        coding = []
        for i, line in enumerate(source, 1):
            if len(line) <= 1:
                continue
            line_info = Program.line_preprocess(i, line, plain=True)
            coding.append(Instruction.to_code(line_info))
    return coding


if __name__ == '__main__':
    print("1) Decode \n2) Encode")
    n = input("Select an option: (1/2) ")
    if n == '1':
        print("1) list of instruction codes \n2) program code")
        m = input("Select an option: (1/2) ")
        if m == '1':
            instruction_codes = eval(input('Enter comma separated instruction codes: (like: 21, 46, 31) '))
        elif m == '2':
            program_code = eval(input('Enter Program code: '))
        else:
            print("Unknown option!")
            exit(-1)
        path = input("Enter output file name: ")
        if m == '1':
            open(path, 'w').write('\n'.join(decode(instruction_codes,factorize=False)))
        else:
            open(path, 'w').write('\n'.join(decode(program_code)))
    elif n == '2':
        path = input("Enter program file path: ")
        print(encode(path),'- 1')


