# 最简单的自定义异常，直接继承 Exception 类
class InsufficientFundsError(Exception):
    """自定义异常，用于表示账户余额不足的错误。"""
    pass

# 定义取款函数
def withdraw(amount):
    if amount > balance:
        raise InsufficientFundsError("余额不足，无法取款")
    return balance - amount

# 异常处理
balance = 100  # 余额变量
try:
    withdraw(150)
except InsufficientFundsError as e:
    print(f"发生错误：{e}")