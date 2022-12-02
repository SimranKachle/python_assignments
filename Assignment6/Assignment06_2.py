# 2.Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that
# amount from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate
# of interest which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0

    def Accept(self):
        self.Name = input("Enter Name: ")
        self.Amount = int(input("Enter Amount: "))

    def Display(self):
        print("The Name is: {} and the Amount is : {}".format(
            self.Name, self.Amount))

    def Deposit(self, value):
        self.Amount = value+self.Amount

    def Withdraw(self, value):
        self.Amount = self.Amount-value

    def CalculateIntrest(self, Time):  # Simple interest formula: (P x r x t) ÷ 100
        Interest = (self.Amount*BankAccount.ROI*Time)/100
        print("Interest is : ", Interest)


def main():
    obj1 = BankAccount()
    obj2 = BankAccount()

    obj1.Accept()
    obj1.Display()
    obj1.Deposit(2000)
    print("The Amount after Depositing 2000 is : ",obj1.Amount)
    obj1.Withdraw(2000)
    print("The Amount after Withdrawing 2000 is : ",obj1.Amount )
    print("The rate of Interest is: ", obj1.CalculateIntrest(5))

    obj2.Accept()
    obj2.Display()
    obj2.Deposit(1000)
    print("The Amount after Depositing 1000 is : ",obj2.Amount),
    obj2.Withdraw(1000)
    print("The Amount after Withdrawing 1000 is : ",obj2.Amount )
    obj2.CalculateIntrest(12)


if __name__ == "__main__":
    main()
