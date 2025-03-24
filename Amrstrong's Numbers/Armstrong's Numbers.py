def is_armstrong_number(number):
    write=str(number)
    lenght=len(write)
    total= sum(int(a)**lenght for a in write)
    return total == number
    
    
