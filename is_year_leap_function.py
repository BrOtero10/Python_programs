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
        

#test

print(is_year_leap(1900))
print(is_year_leap(2000))
print(is_year_leap(2016))
print(is_year_leap(1800))
