A=int(input("Enter a number ="))
B=int(input("Enter a number ="))
#Euclidean Algorithm using while loop
while B !=0:
    A,B=B,A%B
print("GCD is ",A)