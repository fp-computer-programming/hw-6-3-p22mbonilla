# Author MB 11/12/2021

lst = input('enter a list of numbers or letters separated by spaces: ')
lst = list(lst)

end = len(lst) - 1

ans = input('enter is you want the middle or ends: ')

if ans == 'middle':
    print(lst[1:end])
else:
    print(lst[0], lst[end])
