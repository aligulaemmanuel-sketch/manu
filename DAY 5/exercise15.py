# 16. Test if a number is prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 17. Print elements if index AND value are even
def weird_print(lst):
    return [val for i, val in enumerate(lst) if i % 2 == 0 and val % 2 == 0]

# 18. Count types in keyword arguments (**kwargs)
def type_count(**kwargs):
    counts = {}
    for val in kwargs.values():
        t_name = type(val).__name__
        counts[t_name] = counts.get(t_name, 0) + 1
    return ", ".join([f"{k}: {v}" for k, v in counts.items()])

# 19. Custom .split() method
def my_split(text, delimiter=None):
    if delimiter is None:
        return text.split() # Standard whitespace split
    result = []
    current = ""
    for char in text:
        if char == delimiter:
            result.append(current)
            current = ""
        else:
            current += char
    result.append(current)
    return result

# 20. Convert string to password format (*)
def make_password(s):
    return "*" * len(s)