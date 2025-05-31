N=int(input("Enter a number = "))
factors=[]
for i in range(1,N):
    if N%i==0:
        factors.append(i)

print(f"Factors of {N} are {factors}")