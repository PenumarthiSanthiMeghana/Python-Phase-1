i,j,k=0,0,0
arr=[]
tar=0
res=0
for k in range(0,len(arr)-1):
    i=k+1
    j=len(arr)-1
    while(i<j):
        sum=arr[i]+arr[j]+arr[k]
        if sum==tar:
            res=(arr[i],arr[j],arr[k])
            print(res)
            break
        elif sum>tar:
            j=j-1
        elif sum<tar:
            i=i+1
            k=k+1
print(res)