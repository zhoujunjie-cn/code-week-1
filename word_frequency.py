# 统计一段英文里出现频率最高的单词
from collections import Counter
with open("sample.txt","r",encoding="utf-8") as f:
    text=f.read()
words=text.lower().split()
words=[w.strip(".，,!?;:\"'()")for w in words]
words=[w for w in words if len(w)>3]
counter=Counter(words)
for word,count in counter.most_common(10):
    print(f"{word:<15}{count:>5}")