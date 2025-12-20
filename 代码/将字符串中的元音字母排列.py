s=input('输入英文字符串')
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
#tmp放输入里的元音字母
tmp = [ch for ch in s if ch in vowels]
tmp.sort()
s_list = list(s)
idx = 0
for i in range(len(s_list)):
    if s_list[i] in vowels:
        s_list[i] = tmp[idx]
        idx += 1
print(''.join(s_list))
