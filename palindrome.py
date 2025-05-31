N=int(input("Enter a number"))
original=N
reverse=0
while N>0:
    digit=N%10
    reverse=(reverse*10)+digit
    N=N//10
if reverse==original:
    print("Entered number is palindome")
else:
    print("Entered number is not a palindrome number")