"""
题目：张三办了一张银行卡，里面没有一分钱，现在他要进行存钱和取钱的操作
任务：
    1、编写两个函数：存钱函数 --> save_money()和取钱函数 --> get_money()
    2、创建一个bank_card.txt的文本文档，用来充当银行卡


要求：
    1、当调用存钱函数时，我们输入的金额将会存储在bank_card.txt**(银行卡)**中
    2、当调用取钱函数时，我们输入的金额会从bank_card.txt**(银行卡)**中扣除
"""
my_money = 10000


def save_money():
    global my_money
    money_num = int(input("请输入你要存储的金额："))
    if money_num <= my_money:
        # 读取银行卡余额
        with open("bank_card.txt", "r", encoding="utf-8") as file_one:
            money = file_one.read()
        try:
            with open("bank_card.txt", "w", encoding="utf-8") as file_two:
                file_two.write(str(money_num + int(money)))
        except ValueError as e:
            print(e)
            with open("bank_card.txt", "w", encoding="utf-8") as file_two:
                file_two.write(str(money_num + 0))
        print("存钱成功")
    else:
        print("钱包余额不足")


def get_money():
    with open("bank_card.txt", "r", encoding="utf-8") as file_one:
        atm_money = file_one.read()
        print("当前银行卡的余额是{}".format(atm_money))
    money_num = int(input("请输入你要取的金额："))
    if money_num <= int(atm_money):
        with open("bank_card.txt", "w", encoding="utf-8") as file_two:

            # 覆盖,往银行卡写入剩余的金额
            file_two.write(str(int(atm_money) - money_num))
        with open("bank_card.txt", "r", encoding="utf-8") as file_one:
            atm_money_new = file_one.read()
        print(f"取款成功，当前银行卡余额金额为：{atm_money_new}")
    else:
        print("余额不足")


# 实现代码的业务逻辑
def main():
    while True:
        number = int(input("1:存钱  2：取钱  3：退出"))
        if number == 1:
            save_money()
        elif number == 2:
            get_money()
        elif number == 3:
            print("欢迎下次使用~~~~")
            break


# 程序入口
if __name__ == '__main__':
    main()
