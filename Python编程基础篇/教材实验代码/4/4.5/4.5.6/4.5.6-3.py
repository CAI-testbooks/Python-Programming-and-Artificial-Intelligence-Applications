context = '****Python***'
print(context.strip('*'))        # 删除两侧的 *
# 运行结果: Python
print(context.lstrip('*'))       # 删除左侧的 *
# 运行结果: Python***
print(context.rstrip('*'))       # 删除右侧的 *
# 运行结果: ****Python
