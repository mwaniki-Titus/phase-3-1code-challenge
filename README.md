# phase-3-1code-challenge

##challenge-1

The convert_to_24_hour function takes a time string as input, such as "8:30 am" or "8:30 pm".
It first splits the input string into hour and minute_period using the space character as a separator. This results in hour being the hour part and minute_period being the minute part along with the period (am/pm).
The hour is converted to an integer using int(hour).
The minute and period are extracted from minute_period. The minute is obtained by taking all characters except the last two, and the period is obtained by taking the last two characters.
The code then checks if the period is "pm" and the hour is not 12. If so, it adds 12 to the hour to convert it to the 24-hour format.
If the period is "am" and the hour is 12, it sets the hour to 0 (midnight in 24-hour format).
Finally, the function uses f-string formatting to return the result in the format "hhmm", with leading zeros added to ensure a four-digit string.



##challenge-2

The two_positive function counts the number of positive integers among a, b, and c, and returns True if exactly two of them are positive.The two_positive function take three integers, a, b, and c, as arguments.
It creates a list containing a, b, and c, and then uses a list comprehension to iterate through the list and count the number of positive numbers (greater than 0).
The function returns True if the count of positive numbers is exactly 2, indicating that two out of the three numbers are positive.


##challenge-3
The solve function takes a lowercase string s as input.
It initializes two variables: max_value to keep track of the highest value of consonant substrings found, and current_value to calculate the value of the current consonant substring.
The function iterates through each character char in the input string s.
If the character char is not a vowel (i.e., it's a consonant), its value is added to the current_value, calculated by subtracting the ASCII value of 'a' and adding 1.
The max_value is updated with the maximum value between the current max_value and the current_value.
If the character char is a vowel, the current_value is reset to 0 to start calculating the value of the next consonant substring.
Finally, the function returns the max_value, which represents the highest value among the 
