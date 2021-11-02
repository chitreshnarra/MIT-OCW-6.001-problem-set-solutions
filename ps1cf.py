low=0
high=10000
guess = (high + low)/2
guess_percent=guess/10000
annual_salary = float(input("enter your annual salary : "))
x=annual_salary
portion_saved = guess_percent
total_cost = 1000000
semi_annual_raise = 0.07
num_guesses=0
current_saving = 0
down_payment = total_cost*0.25
r = 0.04
months = 0
epsilon = 100
def saving(months,annual_salary,current_saving) :
    while months <= 36 :
    
        if months > 1 and months %6 == 0:
            annual_salary += annual_salary*semi_annual_raise
        current_saving += current_saving*r/12
        current_saving += (annual_salary/12)*portion_saved       
        months += 1
    return current_saving

current_saving =saving(months,annual_salary,current_saving)

if annual_salary*3 < down_payment :
    print('it is not possible to pay down payment in three years')

else :

    while abs(current_saving - down_payment) >= epsilon :
        num_guesses+=1
        if current_saving > down_payment :
            high = guess
            
        else :
            low = guess

        guess = (high+low)/2
        guess_percent = guess/10000   
        current_saving=0   
        portion_saved=guess_percent
        
        current_saving =saving(months,annual_salary,current_saving)         
    
    print('save',guess_percent*100,'percent of your salary')
    print('number of bisection steps:',num_guesses)