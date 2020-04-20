from dict_of_numbers import dict_of_numbers


class BigNumbers:

    def __init__(self, some_dict, height, width, background=' ', mark='*', space=' '):
        assert len(background) == len(mark), 'Background and mark must have the same length.'
        self.dct = some_dict
        self.height = height
        self.width = width
        self.background = background
        self.mark = mark
        self.space = space
        self.field = [[self.background for n in range(self.width)] for m in range(self.height)]

    def put_mark(self, i, j):
        self.field[i][j] = self.mark

    def string_to_plane(self, some_str):
        n = 0
        for num in some_str:
            num = self.dct.get(num)
            if num:
                for i in range(len(num)):
                    for j in range(len(num[i])):
                        if isinstance(num[i][j], int):
                            try:
                                self.field[i][j + n] = self.mark
                            except IndexError:
                                break
                n += len(num[i])
            else:
                raise TypeError(f"Parameter '{some_str}' contents something except numbers.")

    def print_field(self, reverse=False):
        if not reverse:
            for row in self.field:
                print(self.space.join(row))
        else:
            fld = self.field.copy()
            for row in fld:
                for i in range(len(row)):
                    if row[i].startswith(self.background):
                        row[i] = row[i].replace(self.background, self.mark)
                    elif row[i].startswith(self.mark):
                        row[i] = row[i].replace(self.mark, self.background)
            for row in fld:
                print(self.space.join(row))


if __name__ == '__main__':
    test = BigNumbers(dict_of_numbers, 10, 40, background='   ', mark='***', space='')
    test.put_mark(0, 0)
    test.put_mark(8, 5)
    test.string_to_plane('092637')
    test.print_field(reverse=False)
