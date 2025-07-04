# import random  # 匯入random模組

# ans = random.randint(1, 100)

# while True:
#     guess = int(input("請輸入 1 到 100 之間的數字: "))

#     if guess < 1 or guess > 100:
#         print("請輸入 1 到 100 之間的數字。")
#         continue  # 繼續

#     if guess < ans:
#         print("再大一點")
#     elif guess > ans:
#         print("再小一點")

#     if guess == ans:
#         print("猜中了")
#         break

#     # 字典
#     # dict是透過key-value的方式來儲存資料，key是唯一的，value可以重複
#     # dict是無序的，所以無法透過index來取得資料
#     # dict的key必須是不可鰾的資料型態，例如:int,float,string
#     # dict的value可以是任意資料型態
#     # dict的key-value是透過冒號來連接，key:value
#     # dict的key-value是透過逗號來分隔
d = {1: "a", 2: "b", 3: "c"}

#     # 成績登記系統，key是學生名字，value是學生的成績，每個科目有3個成績
# grade = {
#     "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 75]},
#     "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63], "英文": [93, 83, 73]},
#     "小華": {"國文": [86, 76, 66], "數學": [81, 71, 61], "英文": [91, 81, 71]},
# }

# # 取得小明的數學成績 # [85, 75, 65]

# # 取得小美的第一次英文成績 # 93

# # 取得小華的第二次國文成績 # 76
# print(grade=["小明"]["數學"])
# print(grade=["小美"]["英文"][0])
# print(grade=["小華"]["國文"][1])

# 取得dict的key
print(d.keys())
for key in d.keys():
    print(key)
# 取得dict的value
print(d.values())
for value in d.values():
    print(value)
# 取得dict的key-value
print(d.items())
for key, value in d.items():
    print(key, value)
# 刪除dict的kety-value.pop方法
# 如果刪除資料存在，就刪除並回傳value
print(d.pop(1))
# 如果刪除資料不存在，就回傳None
print(d.pop("a", "not found"))
# 如果資料不存在也沒有預設值，就會報錯

# 檢查dict是否有某個key
# in不能存在value
# 跟list必較，in可以檢查的是list的元素與dict的key
print("a" in d)  # True
print("e" in d)  # False

# 比較複雜的dict
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1,2,3]
print(d["a"][0])  # 1
print(d["b"])  # {"c":4,"d":5}
print(d["b"]["c"])  # 4
