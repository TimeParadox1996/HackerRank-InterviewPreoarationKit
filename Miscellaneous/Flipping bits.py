def flippingBits(n):
    return 2**32 - n - 1


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)
        print(result)
