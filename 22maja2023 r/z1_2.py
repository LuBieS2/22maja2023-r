A=[1,1,1,1,4]
B=[]
n=0
w=0
for m, i in enumerate(A):
    if m==len(A)-1:
        if i==A[m-1]:
            n+=1
            B.append(n)
            B.append(i)
        else:
            B.append(1)
            B.append(i)
    if m<len(A)-1:
        if A[m]==A[m+1]:
            n+=1
        else:
            n+=1
            B.append(n)
            B.append(i)
            n=0
print(B)