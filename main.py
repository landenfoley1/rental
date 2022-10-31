total_income = float(input("What will be your total income for the property? "))
income = total_income

print("In this case your renters will be paying for utilites such as: eletric, water, sewer, garbage and gas")
print(" ")

print("Also your renters will be responsable for taking care of the lawn and snow removel")
print(" ")

mortgage= int(input("How much is your morgage per month? "))

taxes = total_income - 150
total_tax = total_income - taxes
print("Estimated tax is")
print(total_tax)

insurance = total_income - 100
total_insurance = total_income - insurance
print("Estimated home insurance")
print(total_insurance)

vacancy = total_income * 0.05
print("Total amount needed to save for vacancy")
print(vacancy)

repairs = total_income * 0.05
print("Total amount needed to save for repairs")
print(repairs)

capEx = total_income * 0.05
print("Total amount needed to save for major repairs")
print(capEx)

property_manager = total_income * 0.1
total_PM = total_income = property_manager
print("Total amount needed to save for a property manager")
print(total_PM)

total_mortgage = total_income - mortgage
mortgage_total = total_income - total_mortgage
print("Your total mortgage")
print(mortgage_total)

total_expenses = total_tax + total_insurance + vacancy + total_PM + repairs + capEx + mortgage_total
print("Your expenses added up")
print(total_expenses)
print(" ")
print("Your total cashflow each month")
cashflow = income - total_expenses
print(cashflow)
print("Your yearly income for the property will be")
yearly_income = cashflow * 12
print(yearly_income)






    
    
    




