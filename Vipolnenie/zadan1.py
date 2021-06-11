#!/usr/bin/env python3
# -*- coding: utf-8 -*-

m = input("Введите предложение")
for i in range(len(m)):
    if (i+1)%3 == 0:
        print(m[i])