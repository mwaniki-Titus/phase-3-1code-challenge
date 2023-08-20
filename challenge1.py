def convert_to_24_hour(time_str):
    hour, minute_period = time_str.split(' ')
    hour = int(hour)
    minute, period = minute_period[:-2], minute_period[-2:]
    
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    return f"{hour:02d}{minute}"

# Test cases
print(convert_to_24_hour("8:30 am"))  # Output: "0830"
print(convert_to_24_hour("8:30 pm"))  # Output: "2030"
