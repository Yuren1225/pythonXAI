print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個有三個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有六個元素的list
print(1, True, 3.14, "hello")  # 這是一個有四個元素的list

# list讀取元素，元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # a

m = [80, 95, 78, 60, 55]
f = [64, 73, 52, 34, 95]
print((m[1] + f[1]) / 2)  # 95/2=47.5

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取2個元素，所以是[1,3,'b']
print(L[::2])
# 就是取index 1到3的元素，不包含index 4，所以是[2,3,'a']
print(L[1:4])
# 就是取index 1到3的元素，不包含index 4，並且每次取2個元素，所以是[2'a']
print(L[1:4:2])

# list取長度，也就是說list中有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6

# list走訪元素
# 可以透過取得index的方式來找到list的資料
# 也可直接把list當作一個範圍來取得資料
# 有兩個方法都可以，但是看使用的情境是否會需要index來決定要用哪一種方式
# L=[1,2,3,"a","b","c"]
# for i in range(len(L)):
#     print(L[i])

# for i in L
#     print(i)


# N = ["amy", "mandy", "peter"]
# for i in range(len(N)):
#     print(f"{i+1}號是{N[i]}")

# A = 1
# for E in N:
#     print(f"{A}號是{E}")
#     A = A + 1

F = ["蘋果", "香蕉", "鳳梨"]
N = [3, 5, 6]
for i in range(len(F)):
    print(f"{F[i]}有{N[i]}個")
