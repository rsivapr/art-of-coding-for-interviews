def sum_multiples_3_5(n):
    sum = 0
    for number in xrange(n):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum

if __name__ == '__main__':
    print sum_multiples_3_5(1000)
