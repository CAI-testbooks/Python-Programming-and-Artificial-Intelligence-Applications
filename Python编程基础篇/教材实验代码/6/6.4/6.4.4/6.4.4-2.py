# 接上一段的异常类定义
class BankError(Exception):
    """通用银行异常基类。"""
    pass

class InsufficientFundsError(BankError):
    """余额不足的异常。"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
    def __str__(self):
        return f"余额不足：当前余额为 {self.balance}，但尝试取款 {self.amount}"

class AccountNotFoundError(BankError):
    """账户未找到的异常。"""
    def __init__(self, account_id):
        self.account_id = account_id
    def __str__(self):
        return f"账户ID为 {self.account_id} 的账户未找到"


# 定义取款函数
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# 定义查找账户函数
def find_account(account_id):
    accounts = {"123": 100}       # 假设仅账户ID为 "123" 存在
    if account_id not in accounts:
        raise AccountNotFoundError(account_id)
    return accounts[account_id]

# 异常处理
try:
    find_account("456")           # 尝试查找不存在的账户
    withdraw(100, 150)            # 尝试取款超出余额的金额
except InsufficientFundsError as e:
    print(f"发生错误：{e}")
except AccountNotFoundError as e:
    print(f"发生错误：{e}")
except BankError as e:
    print(f"银行系统通用错误：{e}")
