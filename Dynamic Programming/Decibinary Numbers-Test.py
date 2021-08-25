def decibinaryNumbers(queries):
    number_sets = dict()
    for num in range(0, 10**6 + 1, 2):
        value = decibinary(num)
        number_sets[value] = number_sets.get(value, []) + [num]

    numbers = list(number_sets.keys())

    num_freq = [0]
    total = 0
    for num in numbers:
        total += len(number_sets[num]) * 2
        num_freq.append(total)
        #print(num, total)   # Test

    output = []
    for x in queries:
        for f in range(len(num_freq)-1):
            if x <= num_freq[f+1]:
                number_set = number_sets[numbers[f]]
                if x <= num_freq[f] + len(number_set):
                    index = x-num_freq[f] - 1
                    output.append(number_set[index])
                else:
                    index = x-num_freq[f] - len(number_set) - 1
                    output.append(number_set[index] + 1)
                break

    return output


def decibinary(x):
    x = list(str(x))
    x.reverse()

    value = 0
    for i in range(len(x)):
        value += int(x[i]) * (2**i)

    return value


def max_2_power(x):
    power = 0
    while x > 2 ** power:
        power += 1

    return power


if __name__ == '__main__':
    q = int(input())

    queries = []
    for q_itr in range(q):
        x = int(input())
        queries.append(x)

    result = decibinaryNumbers(queries)
    for p in result:
        print(p)
