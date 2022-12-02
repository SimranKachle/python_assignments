# 4.Design python application which creates three threads as small, capital, digits.
# All the threads accepts string as parameter.
# Small thread display number of small characters,
# capital thread display number of capital characters and
# digits thread display number of digits.
# Display id and name of each thread.

import threading


def Small(str):
    count = 0
    for i in range(0, len(str)):
        if((str[i] >= 'a' and (str[i] <= 'z'))):
            count = count+1
    print("")
    print("Small Letter Count is: ", count)


def Capital(str):
    count = 0
    for i in range(0, len(str)):
        if((str[i] >= 'A' and (str[i] <= 'Z'))):
            count = count+1
    print("")
    print("Capital Letter Count is: ", count)


def Digit(str):
    count = 0
    for i in range(0, len(str)):
        if(str[i].isdigit()):
            count = count+1
    print("")
    print("Digit Count is: ", count)


def main():
    str = input("Enter the string: ")

    Thread1 = threading.Thread(target=Small, args=(str,))
    Thread2 = threading.Thread(target=Capital, args=(str,))
    Thread3 = threading.Thread(target=Digit, args=(str,))

    Thread1.start()
    print("Id of First thread is :", id(Thread1),
          "and Name of the thread is :", threading.current_thread().name)
    print("")

    Thread2.start()
    print("Id of Second thread is :", id(Thread2),
          "and Name of the thread is :", threading.current_thread().name)
    print("")

    Thread3.start()
    print("Id of Third thread is :", id(Thread3),
          "and Name of the thread is :", threading.current_thread().name)
    print("")

    Thread1.join()
    Thread2.join()
    Thread3.join()


if __name__ == "__main__":
    main()
