import re
import sys
import os

_, file_name, *X = sys.argv
X = list(map(int, X))


def get_line_type(i, line):
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

    if re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*$', line): # matches: [L] v <- v
        _vars = re.findall(r'(\w\d*)', line) # finds variable names
        if len(_vars) == 2: _vars.insert(0, '') # add empty label
        if _vars[1] != _vars[2]:
            raise SyntaxError('Syntax Error in line %d, Cant use v <- w' % i)
        _label = _vars[0]
        _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[1] # convert X1 to python list syntax X[0]
        return 0, _label, _var

    elif re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*\s*\+\s*1$', line): # matches [L] v <- v + 1
        _vars = re.findall(r'(\w\d*)', line)
        if len(_vars) == 3: _vars.insert(0, '')
        if _vars[1] != _vars[2]:
            raise SyntaxError('Syntax Error in line %d, Cant use v <- w + 1' % i)
        _label = _vars[0]
        _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[1]
        return 1, _label, _var

    elif re.match(r'^(\[\w\d*\])?\s*\w\d*\s*<-\s*\w\d*\s*-\s*1$', line): # matches [L] v <- v - 1
        _vars = re.findall(r'(\w\d*)', line)
        if len(_vars) == 3: _vars.insert(0, '')
        if _vars[1] != _vars[2]:
            raise SyntaxError('Syntax Error in line %d, Cant use v <- w - 1' % i)
        _label = _vars[0]
        _var = "%s[%d]" % (_vars[1][0], int(_vars[1][1:]) - 1) if _vars[1] != 'Y' else _vars[1]
        return 2, _label, _var

    elif re.match('^(\[\w\d*\])?\s*IF\s*\w\d*\s*!=\s*0\s*GOTO\s*\w\d*$', line): # matches [L] IF V != 0 GOTO L2
        _vars = re.findall(r'(\w\d*)', line)
        if _vars[0] == 'I': # add empty label
            _vars.insert(0, '')

        _label = _vars[0]
        _var = "%s[%d]" % (_vars[3][0], int(_vars[3][1:]) - 1) if _vars[3] != 'Y' else _vars[3]

        return 3, _label, _var, _vars[-1]
    else: # Unknown line syntax
        raise SyntaxError('Syntax Error in line %d' % i)


def get_instruction(line_info):
    """
    This function gets a line info and generates alternative python code.

    :param line_info: result of get_line_type fucntion    
    :returns: a list of python instructions based on line info
    """
    _type, _label, *_vars = line_info
    if _type == 1: # addition
        _code = []
        if _label: # if line has label
            _code.append("label .{}".format(_label))
        _code.append("{0} = {0} + 1".format(_vars[0])) 
        return _code
    elif _type == 2: # subtraction
        _code = []
        if _label:
            _code.append("label .{}".format(_label))
        _code.append("{0} = {0} - 1".format(_vars[0]))
        _code.append("if {0} < 0: {0} = 0".format(_vars[0])) # variable should never became negative
        return _code
    elif _type == 3: # if statement
        _code = []
        if _label:
            _code.append("label .{}".format(_label))
        _code.append("if {} != 0: goto .{}".format(_vars[0], _vars[1]))
        return _code


with open(file_name) as source:
    instructions = []
    for i, line in enumerate(source, 1):
        if len(line) <= 1:
            continue
        line_info = get_line_type(i, line)
        instruction = get_instruction(line_info)
        instructions.extend(instruction)

instructions.insert(0, 'X = %s' % (str(X))) #define inputs
instructions.append('label .E') # define Exit label
instructions.append('return Y') # to get result of program
program = '\n    '.join(instructions)


with open('template.tmp', 'r') as tmp:
    Program = tmp.read().replace('### code ###', program) # replace generated code in template file and execute result
    # # if you want to save generated file 
    # with open('result.py', 'w') as result:
    #     result.write(Program)
    
    exec(Program)
    
