def response(hey_bob):
    if hey_bob==None or not hey_bob.strip():
        say="Fine. Be that way!"
    elif hey_bob.strip()[-1]=="?":
        if hey_bob.isupper():
            say = "Calm down, I know what I'm doing!"
        else:
            say="Sure."
    elif hey_bob.isupper():
        say = "Whoa, chill out!"
    else:
        say="Whatever."
    return say
            
        
