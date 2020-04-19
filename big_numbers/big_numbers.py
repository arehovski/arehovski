from dict_of_numbers import dict_of_numbers


class BigNumbers:

    def __init__(self, some_dict, height, width, background=' ', mark='*', space=' '):
        self.dct = some_dict
        self.height = height
        self.width = width
        self.background = background
        self.mark = mark
        self.space = space
        self.field = [[self.background + self.space for n in range(self.width)] for m in range(self.height)]

    def put_mark(self, i, j):
        self.field[i][j] = self.mark + self.space

    def string_to_plane(self, some_str):
        n = 0
        for num in some_str:
            for i in range(len(self.dct[num])):
                for j in range(len(self.dct[num][i])):
                    if isinstance(self.dct[num][i][j], int):
                        try:
                            self.field[i][j + n] = self.mark + self.space
                        except IndexError:
                            break
            n += len(self.dct[num][i])

    def print_field(self, reverse=False):
        if not reverse:
            for row in self.field:
                for i in row:
                    print(i, end='')
                print()
        else:
            fld = self.field.copy()
            for row in fld:
                for i in range(len(row)):
                    if row[i].startswith(self.background):
                        row[i] = row[i].replace(self.background, self.mark)
                    elif row[i].startswith(self.mark):
                        row[i] = row[i].replace(self.mark, self.background)
            for row in fld:
                for i in row:
                    print(i, end='')
                print()


if __name__ == '__main__':
    test = BigNumbers(dict_of_numbers, 10, 37)
    test.put_mark(0, 0)
    test.put_mark(8, 5)
    test.string_to_plane('092637')
    test.print_field(reverse=False)
