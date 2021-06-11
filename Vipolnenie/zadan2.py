#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input("Введите предложение")

if s.find('чу') < 0 or s.find('щу') < 0:
    print("Таких буквосочетаний нет")
else:
    if s.find('чу') < s.find('щу'):
        print(s.find('чу'))
    else:
        print(s.find('щу'))


