def has_double(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            if (i == 0 or s[i-1] != s[i]) and (i == len(s) - 2 or s[i+2] != s[i]):
                return True
    return False


def only_increases(s):
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i+1]):
            return False
    return True


print('Expect True: %s' % has_double('11234'))
print('Expect True: %s' % has_double('12344'))
print('Expect True: %s' % has_double('12334'))
print('Expect False: %s' % has_double('1234'))

print('Expect True: %s' % has_double('112233'))
print('Expect False: %s' % has_double('123444'))
print('Expect True: %s' % has_double('111122'))

print('Expect True: %s' % only_increases('1234'))
print('Expect True: %s' % only_increases('12234'))
print('Expect False: %s' % only_increases('1232'))

lower_limit = 147981
upper_limit = 691423

passwords = []
for i in range(lower_limit, upper_limit):
    s = str(i)
    if only_increases(s) and has_double(s):
        passwords.append(s)
print(len(passwords))
