# import time
#
#
# def Insert():
#     a = []
#     for i in range(10000):
#         a.insert(0, i)
#
#
# def Append():
#     a = []
#     for i in range(10000):
#         a.append(i)
#
#
# start = time.time()
# for i in range(50):
#     Insert()
# print("Insert : ", time.time() - start)
#
# start = time.time()
# for i in range(50):
#     Append()
# print("Append : ", time.time() - start)
#
# x = [1, 1, 1, 1, 1]
# for i in range(len(x) - 1, -1, -1):
#     if x[i] == 1:
#         del x[i]
#
# print(x)


alist = [1, 2, 3]
blist = [4, 5, 6]
clist = [7, 8, 9]

dlist = zip(alist, blist, clist)
# flist = zip(clist, dlist)

print(list(dlist))

elist = sum([2 ** x for x in range(64)])
print(elist)
