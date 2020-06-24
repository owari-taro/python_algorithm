


def fibonacci(n:int)->int:
    """
    [summary]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """    
    a=[]
    a.appned(0)
    a.append(1)
    if n>1:
        for i in range(2,n+1):
            a[i]=a[i-1]+a[i-2]
    return a[n]