def withdraw(balance, amount):
    """
    函数用于模拟取款操作，检查取款金额是否合法以及账户余额是否足够。
    参数:
    balance (float): 当前账户余额
    amount (float): 取款金额
    """
    try:
        # 取款金额必须为正数，如果为负数，则显式抛出异常
        if amount <= 0:
            raise ValueError("取款金额必须为正数！")
        # 检查余额是否足够，如果余额不足，则显式抛出异常
        if amount > balance:
            raise ValueError("余额不足，无法取款。")
        # 执行取款操作
        balance -= amount
        print(f"取款成功！您的新余额为: {balance} 元")
    # 捕获到ValueError，并将其赋值给变量e。
    except ValueError as e:
        print(f"取款失败，错误信息: {e}")

balance = 500  # 假设账户当前余额为500元
# 测试样例1：合法取款操作
withdraw(balance, 200)
# --> 取款成功！您的新余额为: 300 元

# 测试样例2：取款金额为负数
withdraw(balance, -50)
# --> 取款失败，错误信息: 取款金额必须为正数！

# 测试样例3：余额不足，取款超过账户余额
withdraw(balance, 600)
# --> 取款失败，错误信息: 余额不足，无法取款。
