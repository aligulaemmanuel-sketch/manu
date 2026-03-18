# 11. Separate integers and strings
def separate_types(lst):
    ints = [x for x in lst if isinstance(x, int)]
    strs = [x for x in lst if isinstance(x, str)]
    return ints, strs

# 12. Is Palindrome
def is_palindrome(s):
    clean_s = s.lower().replace(" ", "")
    return clean_s == clean_s[::-1]

# 13. Count words with length > k
def sum_over_k(sentence, k):
    words = sentence.split()
    return len([word for word in words if len(word) > k])

# 14. Average value in a dictionary
def dict_avg(d):
    values = d.values()
    return sum(values) / len(values) if values else 0

# 15. Common divisors of two numbers
def common_div(a, b):
    divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors