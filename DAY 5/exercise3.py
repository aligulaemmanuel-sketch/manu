# 3. Count upper and lower case letters
def count_case(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return f"Upper: {upper}, Lower: {lower}"