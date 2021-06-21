for i in range(32, 127):
    end_symbol = '' if (i - 1) % 10 else '\n'
    print("{:>3}".format(int(i)), '->', f'{chr(i)}\t', end=end_symbol)
