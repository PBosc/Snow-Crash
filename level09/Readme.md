with open("token", 'rb') as f:
    text = f.read()
    bytes = [c - i for i, c in enumerate(text)][:-1]
    print(''.join(map(chr, bytes)))

f3iji1ju5yuevaus41q1afiuq

s5cAJpM8ev6XHw998pRWG728z