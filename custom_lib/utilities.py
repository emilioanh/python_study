def shift(seq, dimension='right', n=0):
    a = n % len(seq)
    if dimension is 'right':
        return seq[-a:] + seq[:-a]
    else:
        return seq[-(len(seq)-a):] + seq[:-(len(seq)-a)]