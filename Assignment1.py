def shortest_substrings(s, x):
    substrings = []
    for i in range(len(s)):
        for j in range(i + x - 1, len(s)):
            if s[i] == s[j]:
                substring = s[i:j + 1]
                substrings.append(substring)
    if not substrings:
        return "not-found"

    shortest_length = float('inf')
    shortest_substrings_list = []
    for substring in substrings:
        if len(substring) < shortest_length:
            shortest_length = len(substring)
            shortest_substrings_list = [substring]
        elif len(substring) == shortest_length:
            shortest_substrings_list.append(substring)
    if not shortest_substrings_list:
        return "not-found"
    else:
        return " ".join(shortest_substrings_list)
    
# Test cases
s = "abccdbacca"
x = 3
print("x =", x)
print({shortest_substrings(s,x)})
x = 4
print("x =", x)
print({shortest_substrings(s,x)})
x = 5
print("x =", x)
print({shortest_substrings(s,x)})
x = 6
print("x =", x)
print({shortest_substrings(s,x)})
x = 7
print("x =", x)
print({shortest_substrings(s,x)})
x = 8
print("x =", x)
print({shortest_substrings(s,x)})
x = 11
print("x =", x)
print({shortest_substrings(s,x)})