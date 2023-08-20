def solve(s):
    consonant_values = []
    
    for substring in s.split('a'):
        if substring:
            value = sum(ord(c) - ord('a') + 1 for c in substring)
            consonant_values.append(value)
    
    return max(consonant_values)

# Test cases
print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
