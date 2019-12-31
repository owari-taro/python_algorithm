def simple_gcd(a: int, b: int) -> int:
    """最大公約数を計算する"""
    if a < b:
        a, b = b, a
    x = b
    print("a:{},b:{}".format(a,b))
    while True:
        print("x:{}".format(x))
        if a % x == 0 and b % x == 0:
            print("the answer is {}".format(x))
            return x
        x = x-1


if __name__ == "__main__":
    print(simple_gcd(2, 3))
    print(simple_gcd(4, 6))
