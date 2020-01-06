

def prime_test(n: int) -> bool:
    """return true if n is prime """
    m = int(pow(n, 0.5))
    for d in range(2, m+1):
        if n % d == 0:
            return False
    return True






if __name__ == "__main__":
    print(prime_test(121))
