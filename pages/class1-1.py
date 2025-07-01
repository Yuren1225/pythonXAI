# print("hallo")  # This is a simple Python script that prints "hallo" to the console
# means 註解
# (ctrl + ?) means 快速註解
#'''means 多行註解'''
print(True)  # bool 這是布林值 True/False
print(False)  # bool 這是布林值 True/False
print(1)  # int 這是整數
print(1.0)  # float 這是浮點數
print("hallo")  # str 這是字串
# max_value  # max_value 是一個變數

a = 10  # 新增一個儲存空間並取名a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 變更a的值為字串"apple'
print(a)  # 在終端機顯示a所存的值
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 整數除法
print(1 % 1)  # 取餘數
print(2**2)  # 2的2次方
# 優先順序
# 1. ()括號
# 2. **次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減

a = 5
b = "蘋果"
print(f"{b}有{a}個")
# f-string 用於格式化字串，將變數值嵌入字串中
type(True)  # <class 'bool'> 布林值
type(1)  # <class 'int'> 整數
type(1.0)  # <class 'float'> 浮點數
type("hallo")  # <class 'str'> 字串
# type() 函數用於檢查變數的類型

print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int(1.234))  # float轉int
print(float("1.234"))  # str轉float
print(str(1.234))  # float轉str
print(bool(1.234))  # float轉bool

print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

print("輸入開始")
# input()是一個函式，可以讓使用者輸入文字
# ()裡面的文字是提示提示訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入一個數字: ")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()輸入內容都是字串
