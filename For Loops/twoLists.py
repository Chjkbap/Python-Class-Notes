# lst1 = [1,2,3,4,5]
# prod = 1
# for i in lst1:
#     prod*=i # 1 x1 = 1, 1 x2 = 2, 2 x3 =6,.....
#     print(prod)
# print(f"The product {prod}")

aList = [1, 3, 4, 6]
bList = [1, 3, 5, 7]
# listAB = [aList] + [bList]

listAB = [aList [i] *  bList [i] for i in range(len(aList)) ]
print(listAB)