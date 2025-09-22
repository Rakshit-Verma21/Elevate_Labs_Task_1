#Elevate Labs Task 1 
# Date 22/09/2025
#Task 1 :Build a Calculator CLI App.
#Objective:  Create a command-line calculator supporting basic operations.
#Tools:  Python, VS Code / any text editor, terminal.
#Deliverables:   A Python script (calculator.py).

cal_On=True

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a//b
def calculator():
    n1=float(input("Enter The First Number : "))
    sign=input("+ or - or * or / : ")
    n2=float(input("Enter The Second Number : "))
    if(sign=="+"):
        print(f"{n1} {sign} {n2} = {add(n1,n2)}")
    elif(sign=="-"):
     print(f"{n1} {sign} {n2} = {sub(n1,n2)}")
    elif(sign=="*"):
        print(f"{n1} {sign} {n2} = {multi(n1,n2)}")
    elif(sign=="/"):
        print(f"{n1} {sign} {n2} = {div(n1,n2)}")
    else:
        print("Invalid Input")
    code=input("Enter 'exit' to exit the Calculator ").upper()
    if(code=="EXIT"):
        global cal_On
        cal_On=False
while(cal_On):
   calculator()
    


