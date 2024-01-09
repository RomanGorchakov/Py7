#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "b", "h", "j", "l"}
    b = {"b", "c", "h", "l", "r", "v"}
    c = {"j", "k", "n", "t", "z"}
    d = {"b", "i", "k", "v", "w"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    an = u.difference(a)
    bn = u.difference(b)

    y = (an.intersection(bn)).difference(c.union(d))
    print(f"y = {y}")