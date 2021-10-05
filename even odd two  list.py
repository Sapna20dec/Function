def even(a,b):
    i=0
	while i<len(a) and len(b):
		if a[i]%2==0 and b[i]%2==0:
			print("dono even h")
		else:
			print("dono even nahi h")
		i=i+1
a=[2,6,18,10,3,75]
b=[6,19,24,12,3,87]
even(a,b)