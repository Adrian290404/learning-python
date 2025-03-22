def count_zeros(x):
    count = 0
    for i in range(1, x + 1):
        count += str(i).count('0')
    return count