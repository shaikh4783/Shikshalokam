def modify_string(s):
    ascii_values = [ord(char) for char in s]
    modified = [False] * len(s)

    for i in range(len(ascii_values)):
        ascii_val = ascii_values[i]

        if ascii_val % 2 == 0:  # Even ASCII value
            if i + 1 < len(ascii_values) and not modified[i+1]:
                ascii_values[i + 1] += ascii_val % 7
                if ascii_values[i + 1] < 0 or ascii_values[i + 1] > 127:
                  ascii_values[i+1] = 83
                modified[i + 1] = True
        else:  # Odd ASCII value
            if i - 1 >= 0 and not modified[i-1]:
                ascii_values[i - 1] -= ascii_val % 5
                if ascii_values[i - 1] < 0 or ascii_values[i - 1] > 127:
                  ascii_values[i - 1] = 83
                modified[i - 1] = True
        
    return "".join(chr(val) for val in ascii_values)

# Example usage
s = "sHQen}"
result = modify_string(s)
print(result)