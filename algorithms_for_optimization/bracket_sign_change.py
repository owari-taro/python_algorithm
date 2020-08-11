from typing import Callable,Tuple


def bucket_sign_change(df: Callable, a: float,
     b: float, k=2) -> TUple[float,float]:
    """
    [summary]

    Parameters
    ----------
    df : Callable
        [description]
    a : float
        [description]
    b : float
        [description]
    k : int, optional
        [description], by default 2

    Returns
    -------
    TUple[float,float]
        [description]
    """
    if a > b:
        a, b = b, a
    center, half_width = (b+a)/2, (b-a)/2

    while df(a)*df(b) > 0:
        half_width *= 2
        a = center-half_width
        b = center+half_width

    return (a, b)
