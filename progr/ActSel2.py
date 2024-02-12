#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    num_intervals = int(input("Введите количество интервалов: "))
    S = []

    for _ in range(num_intervals):
        start, end = input("Введите интервал [L, R] через пробел: ").split()
        S.append([int(start), int(end)])

    S.sort(key=lambda x: x[1])

    result = [S[0]]

    for i in range(1, len(S)):
        if S[i][0] + 1 > result[-1][1]:
            result.append(S[i])

    print(result)