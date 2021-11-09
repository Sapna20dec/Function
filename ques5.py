def ask():
    a=[1,2,3,4,5]
    b=[2,4,8,6,9]
    i=0
    while i<len(a) and i<len(b):
        if a[i]%2==0 and b[i]%2==0:
            print("even number")
        else:
            print("not even ")
        i=i+1
ask()




def even (a,b):
    if a%2==0 and b%2==0:
        print("dono even ha")
    else:
        print("dono number not ha")

even(20,40)