
keyword argunment :-
def interest(principle,rate,time):
    i=(principle*time*rate)/100
    print('interest=',i)
interest(10,500,2)


# default argunment :-def interest(principle,rate,time):
    i=(principle*time*rate)/100
    print('interest=',i)
interest(10,500,2)

def add (a,b=5):
    c=a+b
    print('addition=',c)
add(10)
add(10,20)




# positional argunment:-
def add(a,b):
    c=a+b
    print("addition=",c)
add(5,6)




# Arbitary positional argunment:
def add(*num):
    z=num[0]+num[1]+num[2]
    print('addition',z)
add(5,2,4)



def add(x,*num):
    z=x+num[0]+num[1]
    print(z)
add(5,2,4)
details(age=20, name="shyam")



def add(x,y):
    z=x+y
    print(1)
add(5,2)





def kid(x,*kids):
    z =x, kids[0], kids[1],kids[2],kids[3]
    print(z)
kid("rohan", "rani", "pinku", "tinku")




# Arbitary Keyword Argunment:
def add(**num):
    z=num["a"]+num["b"]
    print('addition',z)
add(a=2,b=4)



def sum(**kid):
    print(kid['b'])
sum(a='apple',b='asit')



def details(**kids):
    
    print(kids[1])
details(kids1="rohan",kids2="sohan",kids3="mohan")




    



def add(a,b,c,d = 20):
    e=a+b+c+d
    print(e)
add(10,15,30)
add(5,10,20,2)
add(100,50,90,80)




def details(name,age):
    print("name:",name)
    print("age:",age)
details(age=20,name="shyam")


def details(name, age):
    print("name:", name)
    print("age:", age)
details(20,"ram")








