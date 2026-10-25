scores = {'语文': 117, '数学': 123, '英语': 112}

print(scores['语文'])
# 输出: 117

print(scores['物理'])
# 输出: KeyError: '物理'

print(scores.get('物理'))
# 输出: None

# 遍历字典的键
for subject in scores:    # 等价于 for subject in scores.keys():
    print(f'{subject} 的分数是 {scores[subject]}', end='; ')
# 运行结果: 语文的分数是 117; 数学的分数是 123; 英语的分数是 112;

# 遍历键值对 items()
for subject, score in scores.items():
    print(f'{subject} 的分数是 {score}', end='; ')
# 运行结果: 语文的分数是 117; 数学的分数是 123; 英语的分数是 112;

# 只遍历值 values()
for score in scores.values():
    print(score, end='; ')
# 运行结果: 117; 123; 112;
