#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    S = [float(x) for x in input("Введите список чисел через пробел: ").split()]
    result = []

    while S:
        x = float(min(S))
        result.append([x, x + 1])

        S = [num for num in S if num < x or num > x + 1]

    print(result)