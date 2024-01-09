#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    line1 = input("Введите первую строку: ")
    line2 = input("Введите первую строку: ")

    symbol = ""
    count_pair = 0
    for i in range(len(line1)):
        for j in range(len(line2)):
            if line1[i] == line2[j]:
                count_pair += 1
                
            symbol = line1[i]
            
        if count_pair > 0:
            print(symbol, count_pair)
            
        count_pair = 0
        symbol = ""