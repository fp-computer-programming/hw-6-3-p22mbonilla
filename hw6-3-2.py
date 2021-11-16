# Author MB 11/12/2021

lst = input('give me a bunch of numbers: ')
lst = lst.split()
lst = list(lst)
lst2 = lst.copy()
lst.sort()

if lst == lst2:
    print('the list is sorted')
else:
    print('the list is not sorted')
