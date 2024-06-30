class check:
    def __init__(self,n):
        self.n=n
    def ispalindrome(self):
        if self.n==self.n[::-1]:
            print("yes")
        else:
            print("no")
ob1=check("sshss")
ob2=check("sas")
ob1.ispalindrome()
ob2.ispalindrome()