#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    num_edges = int(input("Введите количество рёбер дерева: "))
    T = []

    for _ in range(num_edges):
        start, end = input("Введите [Род. Дочерн.] через пробел: ").split()
        T.append([int(start), int(end)])

    result = []

    max = 0
    for index, item in enumerate(T):
        for j in range(2):
            if item[j] > max:
                max = item[j]

    while T:
        res = []
        for i in range(max, 0, -1):
            count = 0
            for index, element in enumerate(T):
                if element[0] == i or element[1] == i:
                    count += 1
            if count == 1:
                res.append(i)
        i = 0
        while i != len(T):
            if T[i][1] in res:
                T.pop(i)
                i = i - 1
            i = i + 1
        result.append(res)

    print(result)