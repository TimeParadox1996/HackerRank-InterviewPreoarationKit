def superDigit(n, k):
    total = 0
    for x in n:
        total += int(x)

    total = total * k

    if total < 10:
        return total
    else:
        return superDigit(str(total), 1)


if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])

    result = superDigit(n, k)
    print(result)
