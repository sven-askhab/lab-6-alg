#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    S = [float(x) for x in input("Введите числа через пробел: ").split()]
    S.sort()
    result = []
    i = 0
    r = S[0] + 1

    while i < max(S):
        result.append([S[i], S[i] + 1])
        i += 1
        try:
            while S[i] <= r:
                i += 1
            r = S[i] + 1
        except IndexError:
            pass

    print(result)