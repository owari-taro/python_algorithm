
def normal_pow(x: float, n: int) -> float:
    p = x
    for _ in range(n):
        p *= x
    return p


def dp_pow(x: float, n: int)->float:
    """
    calculate exponationation of x with dynamic programing ,which require O(log(n)) time
    Parameters
    ----------
    x : float
        [description]
    n : int
        [description]

    Returns
    -------
    float
        [description]
    """    

    if n == 1:
        return x
    if n % 2 == 0:
        p = dp_pow(x, n/2)
        return p*p
    else:
        p = dp_pow(x, (n-1)/2)
        return x*p*p


if __name__ == "__main__":
    import time
    st = time.time()
    print(normal_pow(4, 1000000000))
    print(time.time()-st)
