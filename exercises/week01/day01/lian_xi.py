# 计算面积
# def area(a: float, b: float) -> float:
#     return a * b
#
# def main():
#     a=input("请输入长：")
#     b=input("请输入宽：")
#     try:
#         a=float(a)
#         b=float(b)
#     except ValueError:
#         print("请输入数字")
#         return
#     A=area(a,b)
#     print(f"面积：{A:.2f}")
#
# if __name__ == "__main__":
#     main()


# 分钟转小时
# def main():
#     a=input("请输入总分钟数：")
#     try:
#         total_minutes=int(a)
#     except ValueError:
#         print("请输入整数")
#         return
#     hours=total_minutes//60
#     minutes=total_minutes % 60
#     print(f"{hours}小时{minutes:}分钟")
#
# if __name__ == "__main__":
#     main()


# 华度转摄氏度
# def fahrenheit_to_celsius(value: float) -> float:
#     return (value - 32) * 5/9
#
# def main():
#     a=input("请输入华度：")
#     try:
#         value=float(a)
#     except ValueError:
#         print("请输入数字")
#         return
#     celsius=fahrenheit_to_celsius(value)
#     print(f"摄氏度：{celsius:.2f}")
#
# if __name__ == "__main__":
#     main()
