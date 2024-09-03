email = input(" Enter Your Email : ")

def charecters(email):
    if len(email) >= 6:
        print("This Is A Valid Email")
    else:
        print("This Is Not A Valid Email")
    if email[0].isalpha():
        print("This is A Valid Email")
    else:
        print("This is not a valid email")
    if "@" in (email) and (email.count("@")==1):
        print("This is a valid email")
    else:
        print("This is not a valid email")
    if "." in email:
        print("This Is a valid email ")
    else:
        print("This is not a valid email")
    if (email[-4]==".") or (email[-3]=="."):
        print("This is valid email ")
    else:
        print("Using Multiple . Aint Alloweded")


charecters(email)