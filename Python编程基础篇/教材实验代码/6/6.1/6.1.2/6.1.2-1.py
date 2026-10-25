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

# 示例1: 缺少右括号，语法错误
print(f"账户余额为 {balance}元"   # 少了右括号，触发 SyntaxError: invalid syntax

# 示例2: 输入非数字，引发ValueError
amount = float(input("请输入取款金额: "))   # 用户输入"五百"，float()转换失败
balance = withdraw(balance, amount)         # 取款"五百"
# 输出: ValueError: could not convert string to float: '五百'
