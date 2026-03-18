# 6. Factorial (Recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 7. Count element in list (without .count())
def list_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# 8. L2-Norm (Square root of sum of squares)
import math
def norm(lst):
    return math.sqrt(sum(x**2 for x in lst))

# 9. Is Monotonic (Always increasing or always decreasing)
def is_mono(lst):
    is_increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    is_decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    return is_increasing or is_decreasing

# 10. Print longest word in a list
def longest_word(words):
    if not words: return
    print(max(words, key=len))