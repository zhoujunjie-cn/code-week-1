import csv
rows = []
# 用try包裹读取文件的代码
try:
    with open("sample.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            word=row.get("word")
            count=row.get("count")
            if not word or not count:
                continue
            word_str=word.strip()
            count_str=count.strip()
            if not word_str or not count_str:
                continue
            rows.append({"word":word_str,"count":int(count_str)})
# 捕获找不到文件的异常
except FileNotFoundError:
    print("文件没找到")
    exit() # 没找到文件就直接退出程序，不执行后面的代码
rows.sort(key=lambda x:x["count"],reverse=True)
# 在打印循环里加了if判断
for row_data in rows[:10]:
    if row_data["count"]>5:
        print(f"{row_data['word']:15s}{row_data['count']}")
total_count=sum([row_data['count']for row_data in rows])
print(f"共{len(rows)}条,总和{total_count}")
# 新增写入result.csv的代码块
with open("result.csv","w",encoding="utf_8_sig",newline="")as f_out:
    writer=csv.writer(f_out)
    # 写入表头
    writer.writerow(["word","count"])
    # 循环写入每一行数据
    for row_data in rows:
        writer.writerow([row_data["word"],row_data["count"]])