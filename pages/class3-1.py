# call by value
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會跟著改變
b[0] = 2
print(a, b)

# list的append
L = [1, 2, 3]
L.append(4)  # 把4加到L的最後面
print()
# list的移除元素有兩種
# 1.使用remove可以移除指定的元素
L = ["a", "b", "c", "d", "e"]
L.remove("a")  # 移除第一個a
# 代表remove會從頭開始找到苻和的元素就會移除
# 如果想要移除所有符合的，可以使用迴圈
for i in L:
    if i == a:
        L.remove(i)
# 2.使用pop，可以移除指定的index元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除index 0的元素
# 代表pop會移除指定的index的元素
# #如果不指定index，則會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)
