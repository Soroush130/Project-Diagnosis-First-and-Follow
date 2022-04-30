import string
lines = []                        
dict_lines = {}         
none_terminals = []        
terminsals = []
First = {}
Follow = {}
# ======================================== Read file input =====================================================
file = open('input.txt', 'r')

list_line = file.readlines()        
for line in list_line:
    new_line = line.replace('\n', '')
    if new_line != '':
        lines.append(new_line)
file.close()
#  =============================================================================================================

# Found None Terminals and split line with ->

for line in lines:
    new_line = line.split('->')
    none_terminals.append(new_line[0])
    dict_lines[new_line[0]] = new_line[1]


# =================================================================
# Found First

def get_terminal(char):
    result_terminals = []
    terminal = dict_lines[char]  
    terminal_split = terminal.split('|')  
    for part in terminal_split:
        len_part = len(part)
        if len_part > 1:
            if part[0] not in none_terminals:
                result_terminals.append(part[0])
            else:
                res_ter = get_terminal(part[0])
                result_terminals.append(res_ter)
        elif len_part == 1:
            if part not in none_terminals:
                result_terminals.append(part)
            else:
                res_ter = get_terminal(part)
                result_terminals.append(res_ter)

    return result_terminals

for char in none_terminals:
    First[char] = get_terminal(char)

# =================================================================

# Found Follow
def get_follow(nt):
    follow_items = []   
    if nt == none_terminals[0]:
        follow_items.append('$')
    else:
        pass

    for part in list(dict_lines.values()):     
        if nt in part:
            for p in part.split('|'):      

                if nt in p:                     
                    index = p.index(nt)
                    if len(p) == 1:
                        value_index = list(dict_lines.values()).index(part)
                        none_terminal = none_terminals[value_index]
                        follow_items.append(First[none_terminal])
                    elif len(p) > 1:
                        if p[len(p)-1] == nt:
                            value_index = list(dict_lines.values()).index(part)
                            none_terminal = none_terminals[value_index]
                            follow_items.append(First[none_terminal])
                        else:
                            none_terminal = p[index+1]
                            if none_terminal not in string.ascii_lowercase:                    
                                follow_items.append(First[none_terminal])
                            else:
                                follow_items.append(none_terminal)
        else:
            continue
    
    return follow_items

for char in none_terminals:
    Follow[char] = get_follow(char)

# print(First)
# print(Follow)