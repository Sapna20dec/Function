def add(a,b):
    i=0
    sum=0
    j=[]
    while i<len(a) and len(b):
	    sum=a[i]+b[i]
	    j.append(sum)
		i=i+1
	print(j)
n=[50,60,10]
m=[10,20,13]
add(n,m)
