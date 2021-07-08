
a = input("a: ")

b = input("b: ")

operator = input("(-,+,*,/):")



if a.isdigit() == float:
    print("ok")
if b.isdigit() == float:
    print("ok")
else:
    print("not ok")

try:
 if operator == "-":
    c= int(a) - int(b)
    print("c=", c)
 elif operator == "+":
        c= int(a) + int(b)
        print("c=", c)
 elif operator == "*":
            c= int(a)*int(b)
            print("c=", c)
 elif operator == "/":
                c= int(a)/int(b)
                print("c=", c)
except ValueError as e:
    print("input number or letter")
except ZeroDivisionError as e:
    print("cannot be divided by zero")

else:
    print("cant calculate")
