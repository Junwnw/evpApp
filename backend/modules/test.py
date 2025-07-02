# test.py
from crawler import get_weibo_hot

results = get_weibo_hot("")  # 可选关键词筛选
print(f"✅ 获取微博热搜：共 {len(results)} 条")
for item in results:
    print("-", item.get("title", item))
