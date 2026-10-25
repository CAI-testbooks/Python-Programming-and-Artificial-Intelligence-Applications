names = ['Tom', 'Jerry', 'Mike']

dict5 = dict.fromkeys(names)
print(dict5)
# 运行结果: {'Tom': None, 'Jerry': None, 'Mike': None}

dict6 = dict.fromkeys(names, 22)
print(dict6)
# 运行结果: {'Tom': 22, 'Jerry': 22, 'Mike': 22}
