def binary_search_first(numbers, target):
    numbers.sort()
    low = 0
    high = len(numbers)
    while low < high:
        mid = (low+high)//2
        if numbers[mid] < target: 
            low = mid+1
        else: 
            high = mid
    return low