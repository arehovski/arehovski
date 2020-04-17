from dict_of_numbers import dict_of_numbers


def field(i, j):
    return [['.' for n in range(j)] for m in range(i)]


def str_num(str_num, dct):
    fld = field(len(dct['0']), len(dct['0'][0] * len(str_num)))
    n = 0
    for num in str_num:
        for i in range(len(dct[num])):
            for j in range(len(dct[num][i])):
                if isinstance(dct[num][i][j], int):
                    fld[i][j + n] = dct[num][i][j]
        n += len(dct[num][i])
    return fld


if __name__ == '__main__':
    fld = str_num('7548963120', dict_of_numbers)
    for row in fld:
        for i in row:
            print(i, end=' ')
        print()
