def is_year_leap(year):
    
    condicional_1 = (year % 4) == 0 #is the year divisible by four?
    condicional_2 = (year % 100) == 0 #is the year divisible by one hundred?
    condicional_3 = (year % 400) == 0 #is the year divisible by four hundreds?
    
    if(condicional_1 and not condicional_2 and not condicional_3):
        return True
        
    elif(condicional_1 and condicional_2 and condicional_3):
        return True
    
    else:
        return False
        

def days_in_month(year, month):
    
    is_leap = is_year_leap(year)
    
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        return 30
        
    elif (month == 2):
        if is_leap:
            return 29
            
        else:
            return 28
    
    else:
        return

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
