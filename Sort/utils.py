def format_input(instr):
    if instr == 'q':
        return
    input_arr = instr.split(',')
    input_arr = list(map(lambda x: int(x), input_arr))
    return input_arr
