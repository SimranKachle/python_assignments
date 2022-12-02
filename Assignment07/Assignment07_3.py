# 3.Design python application which creates two threads as evenlist and oddlist.
# Both the threads accept list of integers as parameter.
# Evenlist thread add all even elements from input list and display the addition.
# Oddlist thread add all odd elements from input list and display the addition.

import threading


def Evenlist(mylist):
    mylist = list(mylist)
    sum = 0
    for i in range(0, int(len(mylist))):
        if((int(mylist[i]) % 2) == 0):
            sum = sum + int(mylist[i])

    print("Sum of Even Elements: ", sum)


def Oddlist(mylist):
    mylist = list(mylist)
    sum = 0
    for i in range(0, int(len(mylist))):
        if((int(mylist[i]) % 2) != 0):
            sum = sum + int(mylist[i])

    print("Sum of Odd Elements: ", sum)


def main():

    mylist = [int(x)
              for x in input("Enter the Numbers Space Separated").split()]

    thread1 = threading.Thread(target=Evenlist, args=(mylist,))
    thread2 = threading.Thread(target=Oddlist, args=(mylist,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
