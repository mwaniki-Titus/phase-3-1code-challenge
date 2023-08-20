def two_positive(a, b, c):
    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2






def two_positive(a, b, c):
    num_positives = sum([1 for num in [a, b, c] if num > 0])
    return num_positives == 2

# Test cases
print(two_positive(2, 4, -3))  # Output: True
print(two_positive(-4, 6, 8))  # Output: True
print(two_positive(4, -6, 9))  # Output: True
print(two_positive(-4, 6, 0))  # Output: False
