
a = input("a: ")

b = input("b: ")

operator = input("(-,+,*,/):")

if a.isdigit() == float:
    print("ok")
if b.isdigit() == float:
    print("ok")
else:
    print(".")



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

else:
    print("cant calculate")
