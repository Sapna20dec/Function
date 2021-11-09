def hersad():
    i=1
    while i<=1000:
        sum=0
        n=i
        while n>0:
            r=n%10
            sum=sum+r
            n=n//10
        if i%sum==0:
            print(i)
        i=i+1
hersad()