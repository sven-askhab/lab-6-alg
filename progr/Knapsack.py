#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    num_props = int(input("Введите количество предметов: "))
    W = int(input("Введите вместимость рюкзака: "))
    props = []

    for _ in range(num_props):
        start, end = input("Введите [Вес, Цена] через пробел: ").split()
        props.append([int(start), int(end)])

    result = []
    props.sort(key=lambda x: (x[1] / x[0]))
    print(props)

    curent_w = 0
    i = len(props) - 1

    while i >= 0:
        if curent_w + props[i][0] <= W:
            curent_w += props[i][0]
            result.append(props[i])
        elif curent_w + props[i][0] > W:
            t = W - curent_w
            coef = t / props[i][0]
            w = props[i][0] * coef
            p = props[i][1] * coef
            result.append([w, p])
            break
        i = i - 1

    print(result)