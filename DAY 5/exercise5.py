# 5. Find max number (without max())
def find_max(lst):
    if not lst: return None
    highest = lst[0]
    for num in lst:
        if num > highest:
            highest = num
    return highest