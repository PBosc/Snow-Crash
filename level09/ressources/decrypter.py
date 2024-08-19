with open("token", 'rb') as f:
    text = f.readline().strip()
    bytes = [c - i for i, c in enumerate(text)]
    print(''.join(map(chr, bytes)))