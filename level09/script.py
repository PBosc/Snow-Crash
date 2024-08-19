with open("token", 'rb') as f:
    text = f.read()
    bytes = [c - i for i, c in enumerate(text)][:-1]
    print(''.join(map(chr, bytes)))