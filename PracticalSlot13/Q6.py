def selection_sort_asc(array):
    for i in range(1, len(array)):
        print('i =', i)
        m = array[i-1]
        print('m=', m)
        if m > min(array[i:]):
            temp = m
            m = min(array[i:])
            index = array[i:].index(m) + i
            print('min =', m)
            array[i-1] = m
            array[index] = temp
            print(f'iteration {i}, swapped {temp} and {m}')
    return array

def sequential_search(array, key):
    count = 0
    for i in range(len(array)):
        if array[i] == key:
            print(f"Found {key} at position {i}")
            count += 1
        else:
            continue
    if not count:
        print(f"{key} not found!")
    return count

def binary_search_recursive(array, key, low, high):
    mid = (low + high) // 2

    if high >= low:
        if array[mid] == key:
            return mid
        
        elif array[mid] > key:
            return binary_search_recursive(array, key, low, mid - 1)

        elif array[mid] < key:
            return binary_search_recursive(array, key, mid + 1, high)
    else:
        return -1

def binary_search_iterative(array, key):
    low = 0
    high = len(array) - 1
    mid = 0

    while high >= low:
        mid = (high + low) // 2
        if array[mid] > key:
            high = mid - 1
        elif array[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1

lst = [5, 3, 7, 9, 5, 12, 42, 1, 6, 8]
print(selection_sort_asc(lst))
sequential_search(lst, 5)
sequential_search(lst, 13)

print(lst[binary_search_iterative(lst, 8)])
print(lst[binary_search_recursive(lst, 8, 0, len(lst)-1)])