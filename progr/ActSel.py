#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    num_intervals = int(input("Введите количество интервалов: "))
    S = []
    for _ in range(num_intervals):
        start, end = input("Введите интервал [L, R] через пробел: ").split()
        S.append([int(start), int(end)])

    result = []
    m = 0

    while len(S) != 0:
        minimum = 10000
        for index, interval in enumerate(S):
            if interval[1] < minimum:
                minimum = interval[1]
                m = interval[0]
        result.append([m, minimum])
        m_range = list(range(m, minimum))
        S = [interval for interval in S if interval[0] not in m_range]

    print(result)