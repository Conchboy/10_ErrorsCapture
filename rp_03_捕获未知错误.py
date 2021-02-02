try:
    num = int(input("请输入一个整数:"))
    result = 8 / num
    print(result)

except ValueError:
    # 错误的处理代码
    print("类型异常,请输入整数")
