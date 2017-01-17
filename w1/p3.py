#s = 'azcbobobegghakl'
s = 'abcdefghijklmnopqrstuvwxyz'
win = s[0]
l = s[0]
for i in range(1,len(s)):
    if s[i] < s[i-1]:
        if len(l) > len(win):
            win = l
        l = s[i]
    else:
        l += s[i]

if len(l) > len(win):
            win = l
print('Longest substring in alphabetical order is: ' + win)