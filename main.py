import math

try:
    print("\nIF ANY NUMBER IS UNKNOWN, TYPE IT'S VALUE AS 0\n")
    user_Choise = input("Side: 1 \nAngle: 2\nDo you want to solve for a side or an angle?: ")
except:
    print("!Invalid choise, please choose 1 or 2!")
    exit()
#Ask user which function they would like to use, 1 being the side solver, 2 being the angle solver.


def solveEq(callback):
    if user_Choise == "1":
        return callback(a,b,c)
    elif user_Choise == "2":
        return callback(A,B,C)




def findSides(a, b, c):
    if a == 0:
            a = math.sqrt(b*b + c*c)
    elif b == 0:
            b = math.sqrt(a*a + c*c)
    elif c == 0:
            c = math.sqrt(a*a + b*b)
    return a, b, c


def findAngles(A, B, C):
    if A == 0:
        A = 180 - B - C
    elif B == 0:
        B = 180 - A - C
    elif C == 0:
        C = 180 - A - B
    return A, B, C




if user_Choise == "1":
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
    except:
        print("!Invalid number value!")
        exit()

    print("\n", solveEq(findSides))


elif user_Choise == "2":
    try:
        A = float(input("Enter the value of A: "))
        B = float(input("Enter the value of B: "))
        C = float(input("Enter the value of C: "))
    except:
        print("!Invalid number value!")
        exit()
    
    print("\n", solveEq(findAngles))
    