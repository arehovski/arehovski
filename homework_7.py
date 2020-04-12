from random import randint as r


# 1

def delete_string(lst):
    return [i for i in lst if not isinstance(i, str)]


# 2
def fib(n):
    fib_lst = []
    if n == 0:
        fib_lst.append(0)
    elif n == 1:
        fib_lst.append(0)
        fib_lst.append(1)
    else:
        fib_lst.append(0)
        fib_lst.append(1)
        i = 2
        while i <= n:
            fib_lst.append(fib_lst[i - 2] + fib_lst[i - 1])
            i += 1
    fib_lst.pop(0)
    return fib_lst


# 3
def square(n):
    return [i ** 2 for i in range(n + 1)]


# 4
def random(n):
    return [r(1, n) for i in range(n)]


# 5
def sum_even(lst):
    lst_even = [i for i in lst if i % 2 == 0]
    return sum(lst_even)


# 6
def find_max(lst):
    lst.sort()
    return lst[-1]


def find_max_2(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] >= max:
            max = lst[i]
    return max


def test():
    assert delete_string([1, 2, 'a', 'b', 4.5]) == [1, 2, 4.5]
    assert delete_string([]) == []
    assert fib(0) == []
    assert fib(1) == [1]
    assert fib(2) == [1, 1]
    assert fib(3) == [1, 1, 2]
    assert fib(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert square(10) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert square(0) == [0]
    assert len(random(10)) == 10
    for i in random(10):
        assert 1 <= i <= 10
    assert random(0) == []
    assert sum_even([i for i in range(11)]) == 30
    assert sum_even([i for i in range(11) if i % 2 != 0]) == 0
    assert find_max([4, 7, 3, 22, 10, 8, 1]) == 22
    assert find_max_2([100, 4, 7, 3, 22, 10, 8, 1, 200]) == 200



if __name__ == '__main__':
    test()
