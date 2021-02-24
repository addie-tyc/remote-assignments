def binary_search_position(numbers, target):
    numbers.sort()
    low = 0
    high = len(numbers)
    mid = low + ((high - low) // 2)
    if numbers[mid] == target:
        return mid
    else:
        while numbers[mid] != target:
            if target < numbers[mid]:
                high = mid-1
                mid = low + ((high - low) // 2)
                if low > high:
                    mid = -1
                    break
            else:
                low = mid+1
                mid = low + ((high - low) // 2)
                if mid >= len(numbers) or low > high:
                    mid = -1
                    break
    return mid
