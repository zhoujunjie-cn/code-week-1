# 统计一段英文里出现频率最高的单词
# 导入collections模块中的Counter类，专门用做数据统计
from collections import Counter
# 导入pathlib里的Path，用来定位“这个脚本自己所在的文件夹”
from pathlib import Path

# BASE = 当前脚本所在目录（week01）。用它拼路径，不受“从哪里运行”影响。
BASE = Path(__file__).parent

# 使用with语句安全打开文件"sample.txt"（只读模式，并制定UTF-8编码）
# with语句：代码执行完毕后会自动关闭文件，不用手动写f.close()
with open(BASE / "sample.txt", "r", encoding="utf-8") as f:
    #读取文件所有内容，并将其作为一个字符串赋值给变量text
    text=f.read()
# text.lower()将文本中所有大小写字母转换成小写
# split()不传参数时，默认以空白字符为分隔符，将文本切割成单词列表
words=text.lower().split()
# 使用列表推导式(List Comprehension)清洗单词
# w.strip("...")会去掉每个单词首尾包含的标点符号
# strip只会移除两端的字符，不会移除单词中的标点
words=[w.strip(".，,!?;:\"'()")for w in words]
# 只保留长度大于3的词
words=[w for w in words if len(w)>3]
# 使用Counter对处理后的单词列表进行计数
counter=Counter(words)
# counter.most_common(10)会返回出现频率最高的前10个词及其次数
for word,count in counter.most_common(10):
    # 使用f-string格式化输出
    # 单词左对齐占15字符宽，次数右对齐占5字符宽
    print(f"{word:<15}{count:>5}")