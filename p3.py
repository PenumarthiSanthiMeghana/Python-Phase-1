class total:
    def __init__(self,n):
        self.n=n
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
        n=str(self.n)
        if n==n[::-1]:
            print("yes")
        else:
            print("no")
ob1=total(22)
ob2=total(24)
ob1.isprime()
ob1.ispalindrome()
ob2.isprime()
ob2.ispalindrome()