try:
    num = int(input("请输入一个整数:"))
    result = 8 / num
    print(result)

except ValueError:
    # 错误的处理代码
    print("类型异常,请输入整数")


except Exception as result:
    print("未知错误 %s" % result)

else:
    print("尝试成功")

finally:
    print("无论是否出现错误都会被执行的代码")

print("--"*10)
