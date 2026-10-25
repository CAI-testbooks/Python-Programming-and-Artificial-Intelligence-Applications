def withdraw(balance, amount):
    """
    函数用于模拟取款操作。
    参数:
    balance (float): 当前账户余额
    amount (float): 取款金额
    """
    balance -= amount
    return balance

balance = 5000    # 余额5000元

# 示例1: 用户输入500
amount = float(input("请输入取款金额: "))    # 用户输入500
balance = withdraw(balance, amount)          # 取款500元
print(f"账户余额为 {balance} 元")             # 输出: 账户余额为 4500.0 元

# 示例2: 用户输入非数字"五百",引发ValueError
amount = float(input("请输入取款金额: "))    # 用户输入"五百"
balance = withdraw(balance, amount)
# 输出: ValueError: could not convert string to float: '五百'
