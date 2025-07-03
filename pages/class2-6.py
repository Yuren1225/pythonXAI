f = open(r"pages\test.txt", "r")  # 開啟檔案
content = f.read()  # 讀取檔案
f.close()  # 關閉檔案
print(content)

##########################
with open(r"pages\test.txt", "r") as f:
    content = f.read()
# 不用寫f.class()，with 幫你自動關好
