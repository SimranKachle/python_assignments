# 5.Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order
# on screen.
# After execution of thread1 gets completed then schedule thread2.


import threading


def printvalue():
    for i in range(51):
        print("Displaying 1 to 50:", i)


def printreverse():
    for i in range(50, -1, -1):
        print("Displaying 1 to 50 in reverse:", i)


def main():

    Thread1 = threading.Thread(target=printvalue, args=())
    Thread2 = threading.Thread(target=printreverse, args=())

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()


if __name__ == "__main__":
    main()
