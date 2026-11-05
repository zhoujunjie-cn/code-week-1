import csv

rows = []
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
rows.sort(key=lambda x:x["count"],reverse=True)
for row_data in rows[:10]:
    print(f"{row_data['word']:15s}{row_data['count']}")
total_count=sum([row_data['count']for row_data in rows])
print(f"共{len(rows)}条,总和{total_count}")