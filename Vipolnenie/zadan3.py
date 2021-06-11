#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input("Введите предложение ")
k = int(input("Введите номер буквы "))
r = input("Введите букву добавления ")
d = s[:k]+r+s[k:]
print(d)
