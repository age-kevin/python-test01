# 菱形
N = 5
# 上半部分
for i in range(N):
    # 第一行
    if i == 0:
        print(' ' * (N - 1 - i) + '*')
    else:
        s = ' ' * (N - 1 - i) + '*' + (i * 2 - 1) * ' ' + '*'
        print(s)

# 下半部分
for i in range(N-1):
    # 最后一行
    if i == N - 2:
        print(' ' * (N - 1) + '*')
    else:
        s = ' ' * (i + 1) + '*' + (N * 2 - 5 - 2 * i) * ' ' + '*'
        print(s)

# 圆
print('太丑了，不想打印了。。。')
