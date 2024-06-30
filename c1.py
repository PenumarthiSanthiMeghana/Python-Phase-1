#i,j=0,len(arr)-1
arr=[]
i,j=0,len(arr)-1
tar=0
res=0
while(i<j):
    sum=arr[i]+arr[j]
    if sum==tar:
        res=([i],[j])
        print(res)
        break
    elif sum>tar:
        j=j-1
    elif sum<tar:
        i=i+1
    else:
        print("not found")
print(res)