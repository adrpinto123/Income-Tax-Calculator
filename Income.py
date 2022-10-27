income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

tax = income * .2
deduction = 10000
deduction2 = dependents * 3000
incometax = tax - deduction - deduction2

print("The income tax is $" + "{:.2f}".format(incometax))
