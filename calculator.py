#project to creat a simple calculator

def sum(num1,num2):
    return num1+num2

#function to subtrat 2 numbers
def sub(num1,num2):
    return num1-num2
#funtion to multiply 2 number 
def mul(num1,num2):
    return num1*num2
# funtion to devide 2 numbers
def dev(num1,num2):
    return num1/num2

#funtion to average 2 numbers
def ave(num1,num2):
    return (num1+num2)/2

print("select the operater:\n" "1. addition\n" "2. subtration\n" "3. multiplication\n" "4.devision\n" "5. average\n")
select =int(input("select a operator from 1,2,3,4,5"))
num1=int(input("enter first number"))
num2=int(input("enter the second nnumber"))
if select == 1 :
    print("number1","+","number2","=")
    print(sum(num1,num2))
elif select == 2 :
    print("number1","-","number2","=")
    print(sub(num1,num2))
elif select == 3 :
    print("number1","*","number2","=")
    print(mul(num1,num2))
elif select == 4 :
    print("number1","/","number2","=")
    print(dev(num1,num2))
elif select == 5 :
    print(("number1","+","number2"), "/","2" "=")
    print(ave(num1,num2))
else :
    print("invalid operations please select again")


