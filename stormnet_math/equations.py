def quad_ecuation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return None
    elif d >= 0:
        x_1 = (- b + d ** 0.5) / (2 * a)
        x_2 = (- b - d ** 0.5) / (2 * a)
        return round(x_1, 4), round(x_2, 4)

