import math
import time


def decibinaryNumbers(queries):
    M = 5
    N = 2 ** M

    arr = [[0 for j in range(M)] for i in range(N)]
    for k1 in range(N):
        arr[k1][0] = 1

    for k2 in range(M):
        arr[0][k2] = 1
        arr[1][k2] = 1

    for n in range(2, N):
        for m in range(1, M):
            for x in range(n, max(-1, n-5*(2**m)), -(2**m)):
                arr[n][m] += arr[x][m-1]

    for line in arr:
        print(line)
    num_freq = [0]
    total = 0
    for num in range(N):
        total += arr[num][-1]
        num_freq.append(total)
        print(num, total)  # Test

    db_numbers = []
    for x in queries:
        #num1 = binary_search(N, num_freq, x)
        for num1 in range(N):
            if x <= num_freq[num1]:
                remain = x - num_freq[num1]
                if num1 != 0:
                    all_db_numbers = all_db_nums("0", num1, int(math.log(num1, 2)) + 1)
                    db_numbers.append(int(all_db_numbers[remain - 1]))
                else:
                    db_numbers.append(0)
                break

    return db_numbers


def all_db_nums(start, n, bits):
    numbers = []
    if bits == 1:
        if n < 10:
            numbers.append(start + str(n))

    else:
        values = [k1 for k1 in range(min(n // (2**(bits-1)), 9)+1)]
        remains = [n - k2 * (2**(bits-1)) for k2 in values]

        for x in range(len(remains)):
            num_set = all_db_nums(start+str(values[x]), remains[x], bits-1)
            # num_set = [str(values[x])+k3 for k3 in num_set]
            numbers += num_set

    return numbers


def binary_search(N, arr, num):
    a, b = 0, N

    mid = 0
    while a != b:
        mid = (a + b) // 2
        value = arr[mid]
        if num < value:
            b = mid
        elif num > value:
            a = mid + 1
        else:
            a = b = mid
            break

    return a - 1


if __name__ == '__main__':
    q = int(input())

    queries = []
    for q_itr in range(q):
        x = int(input())
        queries.append(x)

    start = time.time()
    result = decibinaryNumbers(queries)
    for p in result:
        print(p)
    end = time.time()
    print(end-start)
