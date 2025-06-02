#Randy Easton
#03/01/2024

# edited 6/2/2025 to more closely align with the required assignment
# added function to set cable length rate per feet


'''
Assignment:
Building on the program you developed in Module 1, you will implement if statements for this assignment. In Module 1, you calculated the total cost of fiber cable installation by multiplying the number of feet by $.87. For this assignment, you will evaluate a bulk discount. Modify your program from Module 1 with the following steps:
Display a welcome message for your program.
Capture the number of feet of fiber optic to be installed from the user.
Evaluate the total cost based on the number of feet requested as described below.
If the user purchases more than 100 feet, they are charged $.80 per foot.
If the user purchases more than 250 feet, they will be charged $.70 per foot.
If they purchase more than 500 feet, they will be charged $.50 per foot.
Display the calculated information including the number of feet requested and the company name.
'''





print("Welcome to Foot by The Fiber.\nYour one stop shop for all your fiber cable needs")
strUserName = input("Whom do we have the pleasure of helping today? ")
strCompany = input("What is your Company's name? ")

print("How much Fiber Optic cable would you like to purchase? ")
strInput = input("In Feet: ") #Captures amount to be purchased User must enter in feet
fltInput = float(strInput) #converts input from string to floating-point-integer data type
def cablerate(length):
    # region Decision Tree
        #Decides what to charge user based on inputed length
    if length >= 500:
        return .50
    elif length < 500 and fltInput >= 250:
        return .70
    elif length < 250 and fltInput >= 100:
        return .80
    else:
        return .87 #used to fix validation issues with code (python expects statement where none is needed)
    # endregion Decision Tree
varCharged = cablerate(fltInput)
# region Receipt Area
strCharged = str(varCharged)
print("\nThank you, "+ strUserName +"\nThe Total being billed to "+ strCompany + " is presented below.\n Be advised the price is based on $" + strCharged + " per foot purchased")

fltMath = fltInput * varCharged  # Math
fltCost = round(fltMath, 2)  # Rounds the calculations to nearest 2 decimals
strCost = str(fltCost) #converts integer back to string for purposes of displaying the cost dynamically


print(strUserName + " has purchased "+strInput+ " feet of Fiber optic cable on behalf of " +strCompany +".") #Prints Parties involved and amount of cable purchased
print("The Total is: $"+ strCost) #Display cost
# endregion Receipt Area