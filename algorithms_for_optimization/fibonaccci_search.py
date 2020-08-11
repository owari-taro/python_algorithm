from typing import Callable

def fibonacci_search(f:Callable,a:float,b:float,n:int,eps:float=0.01):
    s=(1-sqrt(5))/(1+sqrt(5))
    phi=(1+ sqrt(5))/2
    rho=1/(phi*(1-s*(n+1))/(1-s*n))

    yd=f(d)
