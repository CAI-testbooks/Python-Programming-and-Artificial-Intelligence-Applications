def withdraw(balance, amount):
    """
    函数用于模拟取款操作，检查取款金额是否合法以及账户余额是否足够。
    参数:
    balance (float): 当前账户余额
    amount (float): 取款金额
    """
    try:
        # 取款金额转换成float型，如果转换失败，抛出ValueError
        amount = float(amount)
        # 检查余额是否足够
        if amount > balance:
            raise ValueError("余额不足，无法取款。")
        # 检查取款金额是否为负数
        elif amount < 0:
            raise ValueError("取款金额不能为负数。")
        # 执行取款操作
        balance -= amount
        print(f"取款成功！您的新余额为: {balance} 元")

    except ValueError as e:
        print(f"取款发生异常: {e}")

    finally:
        print("感谢使用本银行服务。")

# 假设余额为500元
balance = 500
# 测试样例1：合法取款操作
withdraw(balance, 200)
# --> 取款成功！您的新余额为: 300 元
# --> 感谢使用本银行服务。

# 测试样例2：输入一个无法转换为数字的值（如字母）
withdraw(balance, "abc")
# --> 取款发生异常: could not convert string to float: 'abc'
# --> 感谢使用本银行服务。

# 测试样例3：输入一个负数的取款金额
withdraw(balance, -50)
# --> 取款发生异常: 取款金额不能为负数。
# --> 感谢使用本银行服务。