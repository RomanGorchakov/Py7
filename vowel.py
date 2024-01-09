#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "e", "i", "o", "u", "y"}
    b = list(a)

    line = input("Введите строку: ")
    count = 0

    for i in range(len(line)):
        for j in range(len(b)):
            if line[i] == b[j]:
                count += 1

    print(count)