annual_salary = float(input("enter your annual salary"))
portion_saved = float(input('enter the percent of salary to be saved'))
total_cost = float(input('enter the cost of your dream home'))
r = 0.04
months = 0

current_saving = 0
down_payment = total_cost*0.25

while current_saving < down_payment :
    current_saving += current_saving*r/12
    current_saving += (annual_salary/12)*portion_saved
    months += 1


print("number of months :",months)