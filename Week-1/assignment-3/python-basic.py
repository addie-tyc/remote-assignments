def find_max(numbers):
    max = numbers.pop()
    for i in numbers:
        if i > max:
            max = i
    return max

def find_position(numbers, target):
    ans = -1
    for i in range(len(numbers)):
        if numbers[i] == target:
            ans = i
    return i
