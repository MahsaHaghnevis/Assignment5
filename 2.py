#
##
### created by yseeva
##  aug 6th
# second order equation solver

import math
class Color:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
def solve_second(A,B,C):
    delta= math.pow(B,2) -4*A*C
    if delta>0:
          x1=(-B+math.sqrt(delta))/2*A
          x2=(-B-math.sqrt(delta))/2*A
          print(f"TWO ANSWERS \n ANSWERS ARE : \n --- > x1= {x1}  , x2={x2}")
    elif delta==0:
          x3=B/2*A 
          print(f"ONLY ONE ANSWER \n ANSWER IS : \n--> x={x3}")
    else:
          print(f"YOU don't have real number answer beacause delta is {delta} and it's negative so you have complex number answer")


print("-- WELCOME -- \n here we find answers to the desired equation ")
print("please first standardize your very own equation like this = >  ax^2 + bx + c = 0")
print(" ----->  "+Color.BOLD+Color.UNDERLINE+ Color.GREEN+"a"+Color.END+Color.YELLOW+"x^2 + bx + c = 0"+Color.END)
a=float(input("ENTER a  = > "))
print(" ----->" + Color.YELLOW+" x^2 +"+Color.END+Color.BOLD+Color.UNDERLINE+ Color.PURPLE+"b"+Color.END+Color.YELLOW+"x + c = 0"+Color.END)
b=float(input("ENTER b = > "))
print(" ----->"+Color.YELLOW+" x^2 +x +"+Color.END+Color.BOLD+Color.UNDERLINE+ Color.PURPLE+"c"+Color.END+Color.YELLOW+" = 0"+Color.END)
c=float(input("ENTER c = > "))

solve_second(a,b,c)