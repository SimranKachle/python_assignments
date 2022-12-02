# 1.Design python application which creates two thread named as even and odd.
# Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.

import time
import threading


def Even(No):
    for i in range(No+1):
        if (i % 2 == 0):
            print("Even Number:", i)


def Odd(No):
    for i in range(No+1):
        if (i % 2 != 0):
            print("Odd Number:", i)


def main():
    Number = 10

    p1 = threading.Thread(target=Even, args=(Number,))
    p2 = threading.Thread(target=Odd, args=(Number,))

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
