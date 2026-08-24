def celsius_to_fahrenheit(value:float)->float:
    return (value * 9/5) + 32


def main():
    raw = input("请输入摄氏度：")
    try:
        celsius = float(raw)
    except ValueError:
        print("请输入数字")
        return
    fahrenheit=celsius_to_fahrenheit(celsius)
    print(f"华氏温度：{fahrenheit:.2f}")


if __name__ == "__main__":
    main()