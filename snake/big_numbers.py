def field(i, j):
    return [[' ' for n in range(j)] for m in range(i)]


dict_of_numbers = {'0': [['', '', '', 0, 0, '', '', '', ],
                         ['', '', 0, '', '', 0, '', '', ],
                         ['', 0, '', '', '', '', 0, '', ],
                         ['', 0, '', '', '', '', 0, '', ],
                         ['', 0, '', '', '', '', 0, '', ],
                         ['', '', 0, '', '', 0, '', '', ],
                         ['', '', '', 0, 0, '', '', '', ]],

                   '1': [['', '', '', '', 1, '', '', '', ],
                         ['', '', '', 1, 1, '', '', '', ],
                         ['', '', 1, '', 1, '', '', '', ],
                         ['', 1, '', '', 1, '', '', '', ],
                         ['', '', '', '', 1, '', '', '', ],
                         ['', '', '', '', 1, '', '', '', ],
                         ['', '', '', '', 1, '', '', '', ]]}


def str_num(str_num, dct):
    fld = field(len(dct['0']), len(dct['0'][0] * len(str_num)))
    n = 0
    for num in str_num:
        for i in range(len(dct[num])):
            for j in range(len(dct[num][i])):
                if isinstance(dct[num][i][j], int):
                    fld[i][j + n] = dct[num][i][j]
        n += len(dct['0'])
    return fld


fld = str_num('0110110', dict_of_numbers)

for i in fld:
    for j in i:
        print(j, end=' ')
    print()
