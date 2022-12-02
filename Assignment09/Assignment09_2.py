import os


def Read_File(FileName):
    if(os.path.exists(FileName)):

        fd = open(FileName, "r")
        Data = fd.read()
        print("Data from file is ")
        print(Data)
        fd.close()
    else:
        print("File is not existing")
        return


def main():
    print("Enter the file name to display the contents")
    Name = input()
    Read_File(Name)


if __name__ == "__main__":
    main()
