n=int(input('输入需要拆分的数'))
for a in range(1,n):
    if '0' not in str(a)+str(n-a):
        print('可拆分为'+str([a,n-a]))
        break
