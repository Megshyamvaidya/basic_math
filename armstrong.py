N=int(input("Enter a number = "))
original_number=N
sum=0
while N>0:
    digit=N%10
    sum=sum+(digit*digit*digit)
    N=N//10
print(sum)
if sum==original_number:
    print("Entered number is armstrong number")
else:
    print("Entered number is not a armstrong number")