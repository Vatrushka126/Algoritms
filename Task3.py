from math import sqrt

coeff = list(map(int, input().split()))

def func3(coeff, x):
    expr = coeff[0]*x**3+coeff[1]*x**2+coeff[2]*x+coeff[3]
    return expr

def bin_search(coeff):
    left = -10**8
    right = 10**8

    for i in range(100):
        middle = (left + right) / 2

        if func3(coeff, middle) < 0:
            left = middle
        else:
            right = middle

    return middle

print(bin_search(coeff))