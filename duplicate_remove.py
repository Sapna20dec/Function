def z():
    list=['rishabh','rishabh','abhishek','abhishek','divyash']
    i=0
    b=[]
    while i <len(list):
        if list[i] not in b:
            b.append (list[i])
        i=i+1
    print(b)
z()





# def a():
# list1=[2,3,4,6,7,8,6]
# list=[1,2,4,65,87,7]
# list1.extend(list)
# print(list1)
#     i=0
#     b=[]
#     while i <len(list1):
#         if list[i] not in b:
#             b.append (list[i])
#             i=i+1
#     print(b)
# a()