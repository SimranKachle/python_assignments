import os


def Read_File(FileName,str):
    if (os.path.exists(FileName)):
        fd = open(FileName, "r")
        Data = fd.read()
        d=Data.split()
    n=d.count(str)

    if str in Data:
        
        print("Words has appeared ",n," times")
    else:
        print("Word not found")



def main():
    print("Enter the file name ")
    Name = input()
    str = input("Word to look for: ")
    Read_File(Name,str)


if __name__ == "__main__":
    main()