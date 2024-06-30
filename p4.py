class total:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def isprime(self):
        count=0
        for i in range(1,self.n+1):
            if self.n%i==0:
                count=count+1
        if count==2:
            print("yes") 
        else:
            print("no") 
    def ispalindrome(self):
        if self.s==self.s[::-1]:
            print("yes")
        else:
            print("no")
ob1=total(22,"hello")
ob2=total(32,"sas")
ob1.isprime()
ob1.ispalindrome()
ob2.isprime()
ob2.ispalindrome()