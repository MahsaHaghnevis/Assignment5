#
##
### creatd by Yseeva
##  Aug 6th
# star printer
strEven="#*"
strOdd="*#"
def chess_page( row , col):
    for i in range(row):
        for j in range(col):
            if i%2==0:
                print(strEven , end="")
            else:
                print(strOdd, end="")
            
        print()
            

print("_____ WELCOME _____")
n=int(input("---> Input the numbers of rows you want: "))
m=int(input("---> Input the numbers of columns you want: "))
print()

chess_page(n,m)