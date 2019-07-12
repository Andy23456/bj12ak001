# from selenium.webdriver.common.by import By
#
# # loc = [By.ID, "id1"]
# loc = (By.ID, "id1")
# print(loc[0],loc[1])
# print("--" * 20)
# print(*loc)
# import page
#
# print(page.name)

# loc = (1,2)
# loc = 1,2
# print(type(loc))
import os, sys
print("获取模块所在目录：", os.getcwd())
sys.path.append(os.getcwd())
print("默认path目录：", sys.path)