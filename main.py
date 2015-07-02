#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import string


def main():
    while 1:
        clear()
        message = input('Message:\n')
        clear()
        password = input('Password:\n')
        clear()
        
        encrypted = crypt(message, password, 'e')
        decrypted = crypt(message, password, 'd')
        
        print('Message:\n%s\n\n'
              'Encrypted (%s):\n%s\n\n'
              'Decrypted (%s):\n%s\n\n'
              % (message, password, encrypted, password, decrypted))
        input()


def _test():
    message = 'ola, tudo bem?'
    password = 'joga'
    a = crypt(message, password)
    b = crypt(a, password, 'd')
    print(message, a, b)


def clear(n=80):
    print(n * '\n')


def cycle(num, total):
    result = round(total * (num / total - int(num / total)))
    return(result)


def getAlphIndex(symb):
    alphabet = ' ' + string.ascii_lowercase
    index = alphabet.index(symb.lower())
    return(index)


def crypt(text, key, mode='e'):
    alphabet = ' ' + string.ascii_lowercase
    Alphabet = ' ' + string.ascii_uppercase

    if mode == 'e':
        numKeyRing = [getAlphIndex(x) for x in key]
    elif mode == 'd':
        numKeyRing = [(-getAlphIndex(x)) for x in key]

    code = ''
    num = 0
    for symb in text:
        numKeyIndex = num % len(numKeyRing)
        if symb.lower() in alphabet:
            cryptingNum = cycle(numKeyRing[numKeyIndex] +
                                getAlphIndex(symb),
                                len(alphabet))
            if symb in alphabet:
                cryptedSymb = alphabet[cryptingNum]
            elif symb in Alphabet:
                cryptedSymb = Alphabet[cryptingNum]
            num += 1
        else:
            cryptedSymb = symb
        code += cryptedSymb
    return(code)


if __name__ == '__main__':
    main()