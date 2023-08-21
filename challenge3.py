def strength_callculation(s):
    vowels = "bcdfghjklmnopqrstvwxyz"
    max_value = 0
    current_value = 0
    
    for char in s:
        if char not in vowels:
            current_value += ord(char) - ord('a') + 1
            max_value = max(max_value, current_value)
        else:
            current_value = 0
    
    return max_value

input_string = input ("Enter string: ")


result = strength_callculation(input_string)

print("Strength of the string", result)






