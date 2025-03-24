def square(number):
    if number>64 or number<1:
        raise ValueError("square must be between 1 and 64")
    return 1*(2**(number-1))
        
        


def total():
    squares=64
    start=1 
    final =0
    while start<=squares:
        grain=1*(2**(start-1))
        start=start+1
        final=final+grain
    return final
        
