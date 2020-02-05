

def binary_to_decimal(x: int):
    """conbert binary  to decimal"""
    index = len(x)-1
    x = str(x)
    num = 0
    if index < 0:
        raise Exception("not a number")
    while index >= 0:
        num += int(x[index])*(2**index)
        index -= 1
    return num
