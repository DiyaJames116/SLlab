class myclass:
    def __init__(self,str):
        self.str=str
    def func(self):
        str1=self.str
        ll=str1.split()
        ll.reverse()
        lr=" ".join(ll)
        print(lr)
    def count(self):
        count=0
        for i in range(0,len(self.str)):
            if(self.str[i].lower() in ['a','e','i','o','u']):
                count=count+1
        return count

s1=input("Enter String 1 ")
s2=input("Enter String 2 ")
s3=input("Enter String 3 ")
a=myclass(s1)
b=myclass(s2)
c=myclass(s3)
print("The reverse strings are: \n")
a.func()
b.func()
c.func() 
total=a.count()+b.count()+c.count()
print("the number of vowels: ",total)

 