def task18708():
    for n in range(1, 10000):
        bin_n = bin(n)[2:]
        bin_n += str(sum(map(int, bin_n)) % 2)
        bin_n += str(sum(map(int, bin_n)) % 2)
        if int(bin_n, 2) > 85:
            print(n)
            break


task18708()
