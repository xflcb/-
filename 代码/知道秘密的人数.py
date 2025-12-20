from collections import deque
delay=int(input('到第几天泄密'))
forget=int(input('到第几天忘记'))
n=int(input('查询第几天知道秘密的人数（将对结果10**9 + 7 取余后返回）'))
know, share = deque([(1, 1)]), deque([])
know_cnt, share_cnt = 1, 0
for i in range(2, n + 1):
    if know and know[0][0] == i - delay:
        know_cnt -= know[0][1]
        share_cnt += know[0][1]
        share.append(know[0])
        know.popleft()
    if share and share[0][0] == i - forget:
        share_cnt -= share[0][1]
        share.popleft()
    if share:
        know_cnt += share_cnt
        know.append((i, share_cnt))
print((know_cnt + share_cnt)%(10**9+7))
