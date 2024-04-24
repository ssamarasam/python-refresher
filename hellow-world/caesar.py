def caesar(message, key, mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    key = key % 26
    print("key %26 : ", key)

    for i in message:
        templetter = LETTERS.find(i)
        print("templetter: ", templetter)
        if (mode == 'encrypt'):
            templetter += key
        elif mode == 'decrypt':
            templetter -= key

        if templetter >= len(LETTERS):
            templetter -= len(LETTERS)
        elif templetter < 0:
            templetter += len(LETTERS)
        translated += LETTERS[templetter]
    return translated


print("result: ", caesar('ACYBRARY', 2, 'encrypt'))
print("result: ", caesar('CEADTCTA', 2, 'decrypt'))
