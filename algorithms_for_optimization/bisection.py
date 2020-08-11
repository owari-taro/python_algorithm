from tyipng import Callable,Tuple


def bisection(df: Callable, a: float, b: float, eps: float)->Tuple:
    """
    solve df(x) where a<x<b by bisection algorithm


    Parameters
    ----------
    df : Callable
        derivative of univariate function
    a : float
        [description]
    b : float
        [description]
    eps : float
        [description]
    """
    if a > b:
        a, b = b, a
    ya, yb = df(a), df(b)
    if ya == 0:
        return (a, a)
    elif yb == 0:
        return (b, b)
    while b-a > eps:
        mid = (b+a)/2
        y_mid = df(mid)
        if y == 0:
            return (x, x)
        elif y_mid*ya > 0:
            a = mid
        else:
            b = mid
    return (a, b)






