list1 = [1, 2, 2, 3, 4, 5, 6, 3]
list2 = []
for no in list1:
    if no not in list2:
        list2.append(no)
print(list2)
