import time

def check_num(m, params):
    cur_div, x = params
    return m * cur_div >= x


def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1

    return l


def largest_prime_divisor(x: int) -> int:
    cur_divisor = 2
    largest_divisor = 1

    if x > 0:
        while x > 1:
            multiplier = lbinsearch(1, x, check_num, [cur_divisor, x])
            if cur_divisor * multiplier == x:
                largest_divisor = cur_divisor
                x = multiplier
                cur_divisor = 2
            else:
                cur_divisor += 1
            print(multiplier)
    else:
        pass


    return largest_divisor


# print(f'Largest divisor = {largest_prime_divisor(4)}')
print(50 >> 2)