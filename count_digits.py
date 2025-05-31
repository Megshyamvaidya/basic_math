N=int(input("Enter a number ="))
count= 0
while N>0:
    digit=N%10
    count+=1
    N=N//10

print(count)

