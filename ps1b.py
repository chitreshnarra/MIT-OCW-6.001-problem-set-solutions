annual_salary = float(input("enter your annual salary : "))
portion_saved = float(input('enter the percent of salary to be saved : '))
total_cost = float(input('enter the cost of your dream home: '))
semi_annual_raise = float(input('enter the semi annual raise as an decimal : '))

r = 0.04
months = 0

monthly_salary = annual_salary/12

current_saving = 0
down_payment = total_cost*0.25

while current_saving < down_payment :
    
    if months > 1 and months %6 == 0:
        monthly_salary += monthly_salary*semi_annual_raise

    current_saving += current_saving*r/12
    current_saving += (monthly_salary)*portion_saved
    months += 1
    
print("number of months :",months)