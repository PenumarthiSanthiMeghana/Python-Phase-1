def findrecurringnames(allnames,realnames):
    d={}
    for name in allnames:
        sorted_name="".join(sorted(name))
        if sorted_name not in d:
            d[sorted_name]=1
        else:
            d[sorted_name]+=1
    res=[]
    for name in realnames:
        sorted_name="".join(sorted(name))
        if (d[sorted_name])>1:
            res.append(name)
        else:
            return res            