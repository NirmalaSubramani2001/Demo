# # a=int(input("1. Enter a number"))
# # b=int(input("2. Enter a number"))
# # c=a+b
# # print (c)

# # l=[1,2,3,4,5]
# # for i in l:
# #     print (i)

# # l=[1,2,3,4,5]
# # for i in l:
# #    print (i, end = "")


# l=[1,2,3,4,5]
# l[3] = 10
# for i in l:
#    print (i)

import copy
original = [[1, 2], [3, 4]]
print (original)
original [0][0]  = 10
print (original)
shallow = copy.copy(original)
#deep = copy.deepcopy(original)

# Modify a nested item in the shallow copy
shallow[0][0] = 99 

print(f"Original after shallow modification: {original}") # Output: [[99, 2], [3, 4]] - Original IS affected
print(f"Shallow copy: {shallow}")                       # Output: [[99, 2], [3, 4]]

# Modify a nested item in the deep copy
# deep[0][0] = 55

# print(f"Original after deep modification: {original}")     # Output: [[99, 2], [3, 4]] - Original is NOT affected further
# print(f"Deep copy: {deep}")                             # Output: [[55, 2], [3, 4]]


