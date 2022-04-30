# import string
# numbers = '0123456789'
# lower_char = string.ascii_lowercase
x = {'S': 'ADBCd', 'A': 'a|0', 'B': 'b|A|0', 'C': 'c|0|Ba', 'D': 'd|0', 'E':'C|A|D'}
y = ['S','A','B','C','D','E']

def get_terminal(char):  # S
    result_terminals = []
    terminal = x[char]  # 'ABCD'
    terminal_split = terminal.split('|')  # ['ABCD']
    for part in terminal_split:
        len_part = len(part)
        if len_part > 1:
            if part[0] not in y:
                result_terminals.append(part[0])
            else:
                res_ter = get_terminal(part[0])
                result_terminals.append(res_ter)
        elif len_part == 1:
            if part not in y:
                result_terminals.append(part)
            else:
                res_ter = get_terminal(part)
                result_terminals.append(res_ter)

    # print(result_terminals)
    return result_terminals


for char in y:
    print(char)
    print(get_terminal(char))
    print('==============')
