def BinarySearch(lst, key):
    '''Write a recursive searching algorithm to search for a number entered by user in a list of numbers.
'''
    low = 0
    high = len(lst) - 1
    Found = False
    while low <= high and not Found:
        mid = (low + high)//2
        if key == lst[mid]:
            Found = True
        elif key > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if Found == True:
        print('{} is found in the list'.format(key))
    else:
        print('{} is not found in the list'.format(key))
lst = [27, 1, 4, 2, 5, 1000]
sortedlist = lst.sort()
key = int(input('Please enter the key for searching: '))
BinarySearch(lst, key)