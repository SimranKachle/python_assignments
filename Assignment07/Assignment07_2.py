# 2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer.
# Evenfactor thread will display addition of even factors of given number and
# oddfactor will display addition of odd factors of given number.
# After execution of both the thread gets completed main thread should display
# message as “exit from main”.

import threading


def Evenfactor(No):
    sum = 0
    for i in range(1, No):
        if (No % i == 0) and (i % 2 == 0):
            sum = sum+i
    print("Sum_Even", sum)


def Oddfactor(No):
    sum = 0
    for i in range(1, No):
        if (No % i == 0) and (i % 2 != 0):
            sum = sum+i
    print("Sum_Odd", sum)


def main():
    Number = int(input("Enter the Number: "))

    Thread1 = threading.Thread(target=Evenfactor, args=(Number,))
    Thread2 = threading.Thread(target=Oddfactor, args=(Number,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
