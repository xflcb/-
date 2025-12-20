from collections import Counter
mp=Counter(input('输入字符串'))
vowel=max((mp[ch] for ch in mp if ch in 'aeiou'),default=0)
consonant=max((mp[ch] for ch in mp if ch not in 'aeiou'),default=0)
print(vowel+consonant)

