#coding=utf-8

# 小米兔每天都要去公共浴室洗澡，但是有时候公共浴室人太多，需要排队，小米兔想知道它什么时候能洗澡，你可以帮他算算他要多久才能洗完澡吗？
# 公共浴室最多可同时容纳 n 个人洗澡，每个人洗澡的时间为k分钟，多余的人只能在外面排队等候。（ps：保证不会有插队现象出现）
# 小米兔在第a时刻准备好去公共浴室洗澡，问小米兔什么时候才能洗完澡(初始状态：公共浴室为空）。
# 注意：如果有和小米兔同一时刻去公共浴室的。小米兔排到该时刻全部人的后面。（因为小米兔会礼让）
# 输入
# 第一行三个整数n， k， q（1≤ n ≤100,1≤ k ≤50,1≤ q ≤ 1e5）
# 第二行q组整数(每组两个整数x，y代表在x时刻有y人去澡堂洗澡，1≤ x ≤1e5,1≤ y ≤100 ）
# 第三行一个整数a（a含义如上）
# 输出
# 输出小米兔洗完澡的时刻，每组输出占一行。

# 2个人 5分钟 3
# [1 1] [2 1] [3 1]
# 4

# 12

import sys

nums = None
groups = None
wash = None

# for line in sys.stdin:
#     line = line.strip()
#     if nums is None:
#         nums = line.split(' ')
#         continue

#     if groups is None:
#         groups = line.split(' ')
#         continue

#     if wash is None:
#         wash = int(line)
#         continue


def caculator(nums, groups, wash):
    wash_rom = nums[0]
    wash_limit = nums[1]

    count_group = nums[3]
    wait_max_minite = count_group > wash
    wash_num = wash if wait_max_minite else count_group
    time = 0
    waiting_count = 0
    for i in range(wash_num):
        x = groups[i * 2]
        y = groups[i * 2 + 1] 

        # if waiting_count > 0:
        # if y > wash_rom:

        # else:


        


    
print(caculator([2, 5, 3], [1, 1, 2, 1, 3, 1], 4))
        



