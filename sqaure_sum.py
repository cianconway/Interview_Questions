import math

def min_num_squares(n):
    i = math.floor(math.sqrt(n))
    while n % (i*i) != 0 and i > 1:
        i -= 1

    print int(n / (i*i))