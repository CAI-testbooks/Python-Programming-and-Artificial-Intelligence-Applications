# 定义自定义异常类，继承Exception
class InsufficientFundsError(Exception):
    """自定义异常，用于表示账户余额不足的错误。"""

    def __init__(self, balance, amount):
        self.balance = balance        # 当前余额
        self.amount = amount          # 取款金额

    def __str__(self):
        return f"余额不足：当前余额为 {self.balance}，但尝试取款 {self.amount}"

# 定义取款函数
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)   # 触发自定义异常
    return balance - amount

# 初始化账户余额
balance = 100

# 异常处理
try:
    withdraw(balance, 150)         # 尝试取款超过余额的金额
except InsufficientFundsError as e:
    print(f"发生错误：{e}")