#s = 'azcbobobegghakl'
s = 'obzobobohbobobob'
bob = 'bob'
times = 0

for i in range(0, len(s) - len(bob) + 1):
    if s[i : i+3] == bob:
        times += 1
print('Number of times ' + bob + ' occurs is: ' + str(times))