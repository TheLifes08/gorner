def find_dividers(x):
    result = list()

    for n in range(1, abs(x) + 1):
        if x % n == 0:
            result.append(n)

    return result

def is_root(koefs, root):
    summ = 0

    for i in range(len(koefs)):
        summ += (root ** i) * koefs[len(koefs) - 1 - i]

    if summ == 0:
        return True
    else:
        return False
