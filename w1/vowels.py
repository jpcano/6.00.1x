s = 'murcielago'
count = 0
for char in s:
    if char in 'aeiou':
        count = count + 1
print('Number of vowels: ' + str(count))
