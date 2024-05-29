def solution(numbers, target):
    leaves = [0]
    count = 0
    
    for num in numbers:
        temp =[]
        for leaf in leaves:
            temp.append(leaf+num)
            temp.append(leaf-num)
        leaves = temp
    
    for l in leaves:
        if l == target:
            count += 1
    
    return count