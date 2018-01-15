while True:
    try:
        a=int(input('enter the first number:'))
        b=int(input('enter the second number:'))
        print("a+b= %i"% (a+b))
        # print(f"Hi {name} you'll be 100 in {year_100}!")
        break
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")

f = open("C:/Users/anhnguyen/Desktop/ques.txt","w")
c=a+b
print("Hello Bitch the answer is %i"%c, file=f)
print("Hello World", file=f)
"""
this is not code
this is shit
"""
print("This is our new text f", file=f) 
print("and this is another line.", file=f) 
f.write("Why? Because we can.") 
f.close() 