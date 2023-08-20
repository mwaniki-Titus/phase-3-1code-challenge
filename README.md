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
The solve function splits the given string into consonant substrings by splitting on vowels ('a' in this case). It then calculates the value of each consonant substring and returns the maximum value.The solve function takes a lowercase string, s, as input.

Inside the solve function, there's a nested function called get_value. This function calculates the value of a consonant substring by summing up the ordinal values of its characters minus the ordinal value of 'a' and adding 1. This maps 'a' to 1, 'b' to 2, and so on.
The consonant_substrings list is created by splitting the input string s at occurrences of the vowel 'a'. This effectively extracts the consonant substrings.
For each consonant substring, the get_value function is used to calculate its value. The values of all consonant substrings are collected in a list.
The maximum value among the calculated consonant substring values is determined using the max function.
The function returns the maximum value, which is the highest value among the consonant substrings.
