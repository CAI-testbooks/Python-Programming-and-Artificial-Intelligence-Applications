electricity_usage = float(input('请输入每月用电量（度）：'))
if electricity_usage <= 100:
    bill = electricity_usage * 0.5
elif electricity_usage <= 200:
    bill = 100 * 0.5 + (electricity_usage - 100) * 0.75
else:
    bill = 100 * 0.5 + 100 * 0.75 + (electricity_usage - 200) * 1.0
print('您的电费是：%.2f元' % bill)
