def ctof(c):
    return (c*1.8)+32
def ftoc(f):
    return (f-32)/1.8
def ctok(c):
    return (c+273)
def ktoc(k):
    return (k-273)

l=[]
print("1.C to F")
print("2.F to C")
print("3.C to K")
print("4.K to C")
print("5.F to K")
print("6.K to F")
print("7.Exit")
while(1):
    ch=int(input("Enter your choice"))
    if ch==1:
        c=float(input("Enter temp in c"))
        f=ctof(c)
        tup=(c,f)
        l.append(tup)
    elif ch==2:
        f=float(input("Enter temp in f"))
        c=ftoc(f)
        tup=(f,c)
        l.append(tup)
    elif ch==3:
        c=float(input("Enter temp in c"))
        k=ctok(c)
        tup=(c,k)
        l.append(tup)
    elif ch==4:
        k=float(input("Enter temp in k"))
        c=ktoc(k)
        tup=(k,c)
        l.append(k,c)
    elif ch==5:
        f=float(input("Enter temo in f"))
        c=ftoc(f)
        k=ctok(c)
        tup(f,k)
        l.append(tup)
    elif ch==6:
        k=float(input("Enter temp in k"))
        c=ktoc(k)
        f=ctof(c)
        tup=(k,f)
        l.append(tup)
    elif ch==7:
        break
    else:
        print("Invalid choice")
print(l)