# n = 342
# soDaoNguoc = 0
# while n > 0:
#     chu_so_cuoi = n % 10
#     soDaoNguoc = soDaoNguoc * 10 + chu_so_cuoi
#     n = n // 10
#     print(soDaoNguoc)
#     # print(n)
# print(soDaoNguoc)
def number(n):
    result4 = []
    for k in str(n):
        result4.append(int(k))  
    return result4 
def addTwoNumbers(self, l1, l2):
    L1 = len(l1)  
    L2 = len(l2)
    so_dao_nguoc_1 = 0
    so_dao_nguoc_2 = 0
    so_dao_nguoc_3 = 0
    result1 = ""
    result2 = ""

    for i in l1:
        result1 += str(i)
    result1 = int(result1) 
    for j in l2:
        result2 += str(j)
    result2 = int(result2)
    while result1 > 0:
        chu_so_cuoi_1 = result1 % 10
        so_dao_nguoc_1 = so_dao_nguoc_1 * 10 + chu_so_cuoi_1
        result1 = result1 // 10
    while result2 > 0:
        chu_so_cuoi_2 = result2 % 10
        so_dao_nguoc_2 = so_dao_nguoc_2 * 10 + chu_so_cuoi_2
        result2 = result2 // 10
    sum = so_dao_nguoc_1 + so_dao_nguoc_2
    while sum > 0:
        chu_so_cuoi_3 = sum % 10
        so_dao_nguoc_3 = so_dao_nguoc_3 * 10 + chu_so_cuoi_3
        sum = sum // 10
    print(so_dao_nguoc_3)
    return number(so_dao_nguoc_3)
print(addTwoNumbers(0,[2,4,3],[5,6,4]))
# l1=[2,4,3]
# l2=[5,6,4]
# print(so_dao_nguoc_3(n))