#算術指定運算子
a=1
a+=1#a=a+1
print(a)#2
a-=1#a=a-1
print(a)#1
a*=2#a=a*2
print(a)#2
a/=2#a=a/2
print(a)#1
a**=2#a=a**2
print(a)#1
a%=2#a=a%2
print(a)#1
a//=2#a=a//2
print(a)#0

# 優先順序
# 1.() 括號
# 2.** 次方
# 3./ // % 乘 除 取商 取餘數
# 4.+ - 加 減
# 5.== != > < >= <= 比較運算子
# 6.not
# 7.and
# 8.or
# 9.= += -= *= /= //= %= **= 算數指定運算子

#while 循環
#while 循環會執行一次，直到條件做出真
#while 循環會執行一次，直到條件做出假
#while的條件沒有變成真，就會停止執行
i=0
while i<5:
    print(i)

#break 退出循環
#break 可以退出循環，但是只能在循環中使用
i=0
while i<5:
    print(i)
    for j in range(5):
           print(j)
    if i==3:
       break
    1+=1
    for j in range(5):
       print(j)
       break
    
