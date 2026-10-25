# 定义自定义异常类
class InsufficientFundsError(Exception):
    """自定义异常：余额不足"""
    def __init__(self, message="余额不足，无法完成取款操作。"):
        self.message = message
        super().__init__(self.message)

class NegativeAmountError(Exception):
    """自定义异常：金额不能为负"""
    def __init__(self, message="存款金额不能为负数。"):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    """银行账户类，支持存款和取款操作"""
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """存款操作"""
        try:
            if amount < 0:
                raise NegativeAmountError   # 如果存款金额为负，抛出异常
            self.balance += amount
        except NegativeAmountError as e:
            print(f"存款失败：{e}")
        else:
            print(f"存款成功！当前余额：{self.balance}")
        finally:
            print("存款操作结束。")

    def withdraw(self, amount):
        """取款操作"""
        try:
            if amount < 0:
                raise NegativeAmountError   # 如果取款金额为负，抛出异常
            if amount > self.balance:
                raise InsufficientFundsError # 如果余额不足，抛出异常
            self.balance -= amount
        except InsufficientFundsError as e:
            print(f"取款失败：{e}")
        except NegativeAmountError as e:
            print(f"取款失败：{e}")
        else:
            print(f"取款成功！当前余额：{self.balance}")
        finally:
            print("取款操作结束。")

    def check_balance(self):
        """查看余额"""
        print(f"当前余额：{self.balance}")


# 主程序
if __name__ == "__main__":
    account = BankAccount(100)                 # 创建一个初始余额为 100 的银行账户
    account.deposit(50)                        # 存款 50
    account.withdraw(30)                       # 取款 30
    account.withdraw(200)                      # 取款 200 (余额不足)
    account.deposit(-20)                       # 存款 -20 (非法)
    account.check_balance()                    # 查看余额
