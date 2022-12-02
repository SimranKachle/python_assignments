import sys
import os.path


def main():
    print("Enter the Name of First File: ")
    sFile = input()
    print("Enter the Name of Second File: ")
    tFile = input()

    f1 = open(sFile, "r")
    f2 = open(tFile, "r")

    for line1 in f1:
        for line2 in f2:
            if line1 == line2:
                print("file contents are the same")
            else:
                print("file contents are not the same")
            break

    f1.close()
    f2.close()


if __name__ == "__main__":
    main()
