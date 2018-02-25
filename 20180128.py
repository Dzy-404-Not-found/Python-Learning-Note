#!/usr/bin/env.python
#._*_.coding:utf -8._*_
'''
#酒驾减分测试
score=int(input("请输入您的驾照分数："))
Judge=int(input("请输入您的违章序号 超速为1 闯红灯为2:"))
if Judge==1:
    score-=6
else:
    score-=3
print("您的当前驾照分数为：%d"%score)

#密码验证
while(1):
    shenfen=int(input("请输入您的身份 经理为1 老板为2 员工为3"))
    if shenfen==1 or shenfen==2:
        print("欢迎进入数据库：请输入您的账户密码：")
        name=input("姓名：")
        Password=int(input("密码："))
        if name=="DZY" and Password == 123456:
            print("欢迎您!")
        else:
            print("您不具备权限！")
    else:
        print("您没有该权限！")
'''
'''
#猜拳游戏
import random
while(1):
    computer=random.randint(0,2)
    player=int(input("请输入您的选择：0表示剪刀 1表示石头 2表示布"))
    if (computer == 0 and player == 1 ) or (computer == 1 and player == 2) or (computer ==2 and player == 0):
        print("恭喜你赢了")
    elif(computer == player):
        print("平局，再来！")
    else:
        print("手太黑了，洗洗手再来！")
'''

'''
#打印偶数:
i=0
while i <100:
    if(i%2==0):
        print(i)
    i+=1
'''

