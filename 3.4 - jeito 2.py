from random import random

a = 360 * random()


def switch(valor):
    if int(valor) == 0:
        print("0")

    if int(valor) == 1:
        print("1")

    if int(valor) == 2:
        print("2")

    if int(valor) == 3:
        print("3")


switch(int(a / 90))
