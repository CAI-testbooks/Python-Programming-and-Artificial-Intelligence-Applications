# 定义通用的银行异常基类
class BankError(Exception):
    """通用银行异常基类。"""
    pass

# 继承自BankError的余额不足异常
class InsufficientFundsError(BankError):
    """余额不足的异常。"""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"余额不足：当前余额为 {self.balance}，但尝试取款 {self.amount}"

# 继承自BankError的账户未找到异常
class AccountNotFoundError(BankError):
    """账户未找到的异常。"""

    def __init__(self, account_id):
        self.account_id = account_id

    def __str__(self):
        return f"账户ID为 {self.account_id} 的账户未找到"