# for 迴圈
# for會搭配in來使用，in後面會按一個有範圍的東西
# range(5)會產生一個從0到4的數字序列
# i是迴圈裡的變數可以自己取名
# 迴圈變數每回合會從費為裡面取一個資料出來
for i in range(5):
    print(i, end="，")  # 這會印出0到4的數字

#  range可以設定起始值和結束值,但不會包含結束值
#  range(1, 5)會產生1到4的數字序列
for i in range(1, 5):
    print(i, end=" ")  # 這會印出1到4的數字
# range可以設定起始值、結束值與間隔值,但不會包含結束值
# range(1, 10, 2)會產生1到9的奇數序列
for i in range(1, 10, 2):
    print(i, end=" ")  # 這會印出1, 3, 5, 7, 9的數字
# range可以設定起始值、結束值與間隔值,但不會包含結束值

# a = int(input("請輸入一個數字:"))
# b = int(input("請輸入另一個數字:"))
# for i in range(a, b + 1):
#  print(f"{i}號在教室")

# a = int(input("請輸入一個數字:"))
# b = int(input("請輸入另一個數字:"))
# total = sum(range(a, b + 1))
# print(f"從{a}到{b}的總和是: {total}")

a = int(input("請輸入一個數字:"))
b = int(input("請輸入另一個數字:"))
total = 0
for i in range(a, b + 1):
    total = total + i
    # print(f"{total} + {i} = {total + i} ")
    # 這行會印出每次迴圈的總和與當前數字的加總
print(f"{a}加到{b}的總和是: {total}")  # 這行會印出最終的總和
