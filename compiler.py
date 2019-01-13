import re
import sys
import coding

_, file_name, *X = sys.argv
X = list(map(int, X))

#
SNAPSHOT = input('Should i show snapshot? (y/n) ').lower() in ('y', 'yes')




def get_instruction(i, line_info, snapshot):
    """
    This function gets a line info and generates alternative python code.

    :param line_info: result of get_line_type fucntion    
    :returns: a list of python instructions based on line info
    """
    _type, _label, *_vars = line_info
    if _type == 1:  # addition
        _code = []
        if _label:  # if line has label
            _code.append("label .{}".format(_label))
        if snapshot:
            _code.append('snapshot(%d)' % i)
        _code.append("{0} = {0} + 1".format(_vars[0]))
        return _code
    elif _type == 2:  # subtraction
        _code = []
        if _label:
            _code.append("label .{}".format(_label))
        if snapshot:
            _code.append('snapshot(%d)' % i)
        _code.append("{0} = {0} - 1".format(_vars[0]))
        _code.append("if {0} < 0: {0} = 0".format(_vars[0]))  # variable should never became negative
        return _code
    elif _type == 3:  # if statement
        _code = []
        if _label:
            _code.append("label .{}".format(_label))
        if snapshot:
            _code.append('snapshot(%d)' % i)
        _code.append("if {} != 0: goto .{}".format(_vars[0], _vars[1]))
        return _code


with open(file_name) as source:
    MAX_Z = max(list(map(int, re.findall(r"Z(\d+)", source.read()))) + [0])
    source.seek(0)
    instructions = []
    for i, line in enumerate(source, 1):
        if len(line) <= 1:
            continue
        line_info = coding.Program.line_preprocess(i, line)
        instruction = get_instruction(i, line_info,SNAPSHOT)
        instructions.extend(instruction)

instructions.insert(0, 'show_snapshot = %s' % (str(SNAPSHOT)))  # set snapshot 
instructions.insert(1, 'X = %s' % (str(X)))  # define inputs
instructions.insert(2, 'Z = %s' % (str([0] * MAX_Z)))
if SNAPSHOT:
    instructions.insert(3, 'init_snapshot()')
    instructions.insert(4, 'snapshot(0)')

instructions.append('label .E1')  # define Exit label
instructions.append('return Y')  # to get result of program
program = '\n    '.join(instructions)

with open('template.tmp', 'r') as tmp:
    Program = tmp.read().replace('### code ###', program)  # replace generated code in template file and execute result
    # # if you want to save generated file 
    with open('result.py', 'w') as result:
        result.write(Program)
    exec(Program)
