def uppercase(str):
    willy = ""
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            a = ord(a) - 32
            willy += chr(a)
        else:
            willy += a
    print(willy)
