import os


def Read_File(FileName):
    if(os.path.exists(FileName)):
        print("File Exists")
    else:
        print("File is not existing")
        return


def main():
    print("Enter file name to check")
    Name = input()
    Read_File(Name)


if __name__ == "__main__":
    main()
