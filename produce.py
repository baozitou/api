
with open('/Users/duxy/Desktop/ones-api/test.txt','wt') as f:
    for i in range(100000):
        print('a', file=f, end='')