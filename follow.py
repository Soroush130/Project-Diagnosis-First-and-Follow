import string
x = {'S': 'ADBCd', 'A': 'a|0', 'B': 'b|A|0', 'C': 'c|0|Ba', 'D': 'd|0'}

y = ['S','A','B','C','D']

first = {'S': [['a', '0']], 'A': ['a', '0'], 'B': ['b', ['a', '0'], '0'], 'C': ['c', '0', ['b', ['a', '0'], '0']], 'D': ['d', '0']}


def get_follow(nt):
    follow_items = []    # ['d', '0'] , ['b', ['a', '0'], '0']
    if nt == y[0]:
        follow_items.append('$')
    else:
        pass

    for part in list(x.values()):          # ['ADBCd','a|0','b|A|0','c|0|Ba','d|0']
        if nt in part:
            for p in part.split('|'):       # ['c','0','Ba']

                if nt in p:                     #  p == 'Ba'
                    index = p.index(nt)  # 2
                    # len(p) == 2
                    if len(p) == 1:
                        value_index = list(x.values()).index(part)
                        none_terminal = y[value_index]
                        follow_items.append(first[none_terminal])
                    elif len(p) > 1:
                        if p[len(p)-1] == nt:
                            value_index = list(x.values()).index(part)
                            none_terminal = y[value_index]
                            follow_items.append(first[none_terminal])
                        else:
                            none_terminal = p[index+1]
                            if none_terminal not in string.ascii_lowercase:                    
                                follow_items.append(first[none_terminal])
                            else:
                                follow_items.append(none_terminal)
        else:
            continue
    
    return follow_items

for char in y:
    print(f'Follow({char}) = {get_follow(char)}')
    print("===============================")