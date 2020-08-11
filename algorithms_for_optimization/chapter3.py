from typing import Callable,Tuple

def bracket_minimmum(f:Callable,x:float=0,s:float=1e-2,
    k=2.0:float)->Tuple[float,float]:
    """
    [summary]

    Parameters
    ----------
    f : Callable
        [description]
    x : float, optional
        [description], by default 0
    s : float, optional
        [description], by default 1e-2
    k : [type], optional
        [description], by default 2.0:float

    Returns
    -------
    Tuple[float,float]
        [description]
    """

    a,ya=x,f(x)
    b,yb=a+s,f(a+s)
    if yb>ya:
        a,b=b,a
        ya,yb=yb,ya
        s=-1*s
    while True:
        c,yc=b+s,f(b+s)