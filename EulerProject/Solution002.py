def fibonacci_evensum(cap):
    fibtail = [1,2]
    if cap <= 1:
        return 0
    else:
        sum = 2
        last = 2
        while last < cap:
            last = fibtail[-1] + fibtail[-2]
            if last > cap:
                return sum
            else:
                fibtail[-2], fibtail[-1] = fibtail[-1], last
                if last % 2 == 0:
                    sum += last
    return sum

if __name__ == '__main__':
    print fib_list(4000000)
