def quad_equation(a, b, c):
    """
    Returns the roots of quadratic equation or none if discriminant less than 0.
    quad_equation(4, 4, 1)
    (-0.5, -0.5)
    quad_equation(4, 4, 2)
    None
    quad_equation(4, 8, 2)
    (-0.2929, -1.7071)
    """
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return None
    elif d >= 0:
        x_1 = (- b + d ** 0.5) / (2 * a)
        x_2 = (- b - d ** 0.5) / (2 * a)
        return round(x_1, 4), round(x_2, 4)
