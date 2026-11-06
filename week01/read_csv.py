# 导入python内置的csv模块，用于读取和写入csv格式文件
import csv
# 创建一个空列表，用来准备存储后续从文件读取出来的所有数据行
rows = []
# 用try包裹读取文件的代码块，用于捕获文件不存在时的异常
try:
    # with语句安全打开sample.csv，指定只读模式"r"，并处理文件编码
    # encoding="utf-8-sig"专门用于处理可能带有BOM头的UTF-8文件（常用于Excel导出的csv）
    with open("sample.csv", "r", encoding="utf-8-sig") as f:
        # 使用csv.DictReader将打开的文件转换成字典格式读取器
        # 这样读取出来的每一行都会是一个字典，键是表头（如word，count）
        reader = csv.DictReader(f)
        # 遍历读取器，每次循环提取一行数据赋值给变量row
        for row in reader:
            # 使用.get()方法尝试获取"word"键的值，如果不存在则返回None（防止KeyError报错）
            word=row.get("word")
            # 同理获得"count"键的值
            count=row.get("count")
            # 如果word或count任意一个为空（None或空字符串），则跳过当前循环
            if not word or not count:
                continue
            # 调用字符串的strip()方法，去除获取到的word首尾可能存在的空格或换行符
            word_str=word.strip()
            # 同理，去除count首尾的空格
            count_str=count.strip()
            # 去除空格后再次检查，防止原本只有空格的脏数据混入
            if not word_str or not count_str:
                continue
            # 将处理好的干净数据以字典的形式追加到rows列表中
            # 将count转换成整数(int)，方便后续进行数值排序和加减运算
            rows.append({"word":word_str,"count":int(count_str)})
# 捕获找不到文件的异常
except FileNotFoundError:
# 如果文件不存在，在终端打印提示而不是直接报错
    print("文件没找到")
# 没找到文件就直接退出程序，不执行后面的代码
    exit()
# 使用列表的sort()方法对rows进行排序
# key=lambda x:x["count"]表示按照字典中"count"的值进行排序
# reverse=True表示降序排列
rows.sort(key=lambda x:x["count"],reverse=True)
# 在打印循环里加了if判断，只遍历前10条数据
for row_data in rows[:10]:
    # 如果这行数据的count大于5，才执行打印
    if row_data["count"]>5:
        # 使用f-string格式化输出：word左对齐占15个字符宽，count正常输出
        print(f"{row_data['word']:15s}{row_data['count']}")
# 遍历所有rows，提取出每个字典的"count"值，使用sum()计算总和
total_count=sum([row_data['count']for row_data in rows])
# 打印总共有多少条数据，以及所有count的总和
print(f"共{len(rows)}条,总和{total_count}")
# 新增写入result.csv的代码块
# 打开或创建result.csv文件，"w"表示写入模式
# newline=""是必不可少的参数，防止Windows下写入时每行之间多出空行
with open("result.csv","w",encoding="utf_8_sig",newline="")as f_out:
    # 创建一个csv.writer对象，用于将数据写入文件
    writer=csv.writer(f_out)
    # 写入表头：这里是一个列表，里面包含"word"和"count"
    writer.writerow(["word","count"])
    # 循环遍历之前存好数据的rows列表
    for row_data in rows:
        # 按行写入数据，将字典中的word和count提取出来组成列表写入文件
        writer.writerow([row_data["word"],row_data["count"]])