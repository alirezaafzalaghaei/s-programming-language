import re
import sys
import os

_, file_name, *X = sys.argv
X = list(map(int, X))


def get_line_type(i, line):
    if line.islower():
        raise SyntaxError('Syntax Error in line %d. You should use UPPERCASE letters' % i)

    if re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*$', line):
        _vars = re.findall(r'(\w\d*)', line)
        if len(_vars) == 2: _vars.insert(0, '')
        if _vars[1] != _vars[2]:
            raise SyntaxError('Syntax Error in line %d, Cant use v <- w' % i)
        _label = _vars[0]
        _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[1]
        return 0, _label, _var

    elif re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*\s*\+\s*1$', line):
        _vars = re.findall(r'(\w\d*)', line)
        if len(_vars) == 3: _vars.insert(0, '')
        if _vars[1] != _vars[2]:
            raise SyntaxError('Syntax Error in line %d, Cant use v <- w + 1' % i)
        _label = _vars[0]
        _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[1]
        return 1, _label, _var

    elif re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*\s*-\s*1$', line):
        _vars = re.findall(r'(\w\d*)', line)
        if len(_vars) == 3: _vars.insert(0, '')
        if _vars[1] != _vars[2]:
            raise SyntaxError('Syntax Error in line %d, Cant use v <- w - 1' % i)
        _label = _vars[0]
        _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[1]
        return 2, _label, _var

    elif re.match('^(\[\w\d*\])?\s*IF\s*\w\d*\s*!=\s*0\s*GOTO\s*\w\d*$', line):
        _vars = re.findall(r'(\w\d*)', line)
        if _vars[0] == 'I':
            _vars.insert(0, '')

        _label = _vars[0]
        _var = "%s[%d]" % (_vars[3][0], int(_vars[3][1:]) - 1) if _vars[3] != 'Y' else _vars[3]

        return 3, _label, _var, _vars[-1]
    else:
        raise SyntaxError('Syntax Error in line %d' % i)


def get_instruction(line_info):
    _type, _label, *_vars = line_info
    if _type == 1:
        _code = []
        if _label:
            _code.append("label .{}".format(_label))
        _code.append("{0} = {0} + 1".format(_vars[0]))
        return _code
    elif _type == 2:
        _code = []
        if _label:
            _code.append("label .{}".format(_label))
        _code.append("{0} = {0} - 1".format(_vars[0]))
        _code.append("if {0} < 0: {0} = 0".format(_vars[0]))
        return _code
    elif _type == 3:
        _code = []
        if _label:
            _code.append("label .{}".format(_label))
        _code.append("if {} != 0: goto .{}".format(_vars[0], _vars[1]))
        return _code


with open(file_name) as source:
    instructions = []
    for i, line in enumerate(source, 1):
        if len(line) == 1:
            continue
        line_info = get_line_type(i, line)
        instruction = get_instruction(line_info)
        instructions.extend(instruction)

instructions.insert(0, 'X = %s' % (str(X)))
instructions.append('label .E')
instructions.append('return Y')
program = '\n    '.join(instructions)


with open('template.tmp', 'r') as tmp:
    Program = tmp.read().replace('### code ###', program)
    with open('result.py', 'w') as result:
        # result.write(Program)
        # exec(open("result.py").read())
        pass
    exec(Program)
