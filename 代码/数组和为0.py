n=int(input('输入需要的数组长度'))
ans=[]
for i in range(1,n//2+1):
    ans.append(i)
    ans.append(-i)
if n%2==1:
   ans.append(0)
print('满足条件的数组为'+str(ans))
