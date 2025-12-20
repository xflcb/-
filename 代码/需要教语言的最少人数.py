x=int(input('总共有几种语言？'))
n=int(input('请输入用户数量：'))
languages=[]
for i in range(n):
    langs=list(map(int,input(f'请输入用户{i+1}掌握的语言（用空格分隔，语言不得超过总语言数）：').split()))
    languages.append(langs)
m=int(input('请输入朋友关系的数量：'))
friendships=[]
for i in range(m):
    u,v=map(int,input(f'请输入第{i+1}个朋友关系（两用户ID用空格分隔）').split())
    friendships.append([u,v])
cncon=set()
for friendship in friendships:
    mp={}
    conm=False
    for lan in languages[friendship[0]-1]:
        mp[lan]=1
    for lan in languages[friendship[1]-1]:
        if lan in mp:
            conm=True
            break
    if not conm:
        cncon.add(friendship[0]-1)
        cncon.add(friendship[1]-1)
max_cnt=0
cnt=[0]*(n+1)
for friendship in cncon:
    for lan in languages[friendship]:
        cnt[lan]+=1
        max_cnt=max(max_cnt,cnt[lan])
print('需要教语言的最少人数为'+str(len(cncon)-max_cnt)+'人')
