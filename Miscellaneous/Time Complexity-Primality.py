import math


def primality(n):
    if n > 2:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return "Not prime"

        return "Prime"
    elif n == 2:
        return "Prime"
    else:
        return "Not prime"



if __name__ == '__main__':
    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)
        print(result)
