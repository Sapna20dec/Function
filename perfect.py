def a():
    num = int(input("enter a number"))
    i = 1
    sum = 0
    while i < num:
	    if num % i == 0:
		    sum = sum+i
	    i = i+1
    if num == sum:
	    print(num, "is a perfect number")
    else:
	    print(num, "is a not perfect number")
a()







def a():
    i=1
    while i<=1000:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum=sum+j
            j=j+1
        if sum==i:
            print(i)
        i=i+1 
a()  

