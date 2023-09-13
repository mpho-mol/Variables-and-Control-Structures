import math


print("investment- to calculate the amount of interest you'll earn on interest")

print("bond- to calculate the amount you'll have to pay on a home loan")

print("Enter either ‘investment’ or ‘bond’ from the menu above to proceed:")


choice = input()


if  choice == "investment" or choice == "Investment" or choice == "INVESTMENT": #So entry will not be case sensitive, all the listed will be valid entries

    P = float(input("Enter the deposit amount: ")) #Principal amount

    r = float(input("Enter the rate of interest: ")) #Enter as decimal, 0.08 instead of 8%

    t = int(input("Enter the time in years: "))

    interest_type = input("Enter the type of interest: \nSimple \nCompound \n")


    if interest_type == "Simple":

        A = P * (1 + r*t)
        print("The amount after " + str(t) + " years is " + str(round(A,2)))

    elif interest_type == "Compound":

         A = P * math.pow((1 + r), t)
         print("The amount after " + str(t) + " years is " + str(round(A,2)))

    else:

        print("Invalid")

    

elif choice == "bond" or choice == "Bond" or choice == "BOND":

    P = float(input("Enter the present value of the house: "))

    r = float(input("Enter the rate of interest: "))

    n = int(input("Enter the number of months for the bond: "))

    i = n/12

    repayment = (i * P)/(1 - (1 + i)**(-n))

    print("The repayment after ", str(n), " months is ", str(round(repayment,2)))




else:

    print("Invalid")

 
