plant = 'rose'
palin = "stats"
temp_str = ''
for char in palin[::-1]:
    temp_str = str(temp_str + char)
    print(char)
print(temp_str)
print(palin)
if palin == temp_str:
    print("it's a palindrome")
else:
    print("Guess it's not? (sucks to suck)")
