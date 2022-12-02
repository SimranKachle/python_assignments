import os

def main():
         print("Enter the Name of Source File(For Reading): ")
         sFile = input()
         print("Enter the Name of Target File: ")
         tFile = input()
         fileHandle = open(sFile, "r")
         texts = fileHandle.readlines()
         fileHandle.close()

         fileHandle = open(tFile, "w")
         for s in texts:
            fileHandle.write(s)
            fileHandle.close()
    
    
if __name__=="__main__":
    main()




