# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


from operator import add, sub
from random import randint, choice

# 设置数组，符号和函数名的转换
ops = {'+': add, '-': sub}
# 只能容忍连续两次输入错误
MAXTRIES = 2


def doprob():
    # choice()方法返回一个列表，元组或字符串的随机项。
    op = choice('+-')
    # for循环两次，生成拥有两个1-10之间的随机数的数组
    nums = [randint(1, 10) for i in range(2)]
    # 数组内部排序，升序排序然后反转
    nums.sort(reverse=True)
    # op是+—其中一个符号，ops[op]获取相应的函数，* 用来传递任意个无名字参数，这些参数会一个Tuple的形式访问
    # 执行函数，例如：add((1,2))，ans存储结果
    ans = ops[op](*nums)
    # 拼接一个数学计算的字符串
    pr = '%d %s %d=' % (nums[0], op, nums[1])
    # 用户连续输入错了几次结果
    oops = 0
    # 一直循环下去接受指令
    while True:
        try:
            # 接受用户的输入，判断是否等于程序计算出来的结果
            # 输入结果正确，输出correct
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            # 判断用户是否连续输错了两次结果，如果是，则告诉用户正确结果
            if oops == MAXTRIES:
                print 'sorry... the answer is\n%s%d' % (pr, ans)
            # 如果没有两次，则提示不正确，继续输入，并且错误次数+1
            else:
                print 'incorrect... try again'
                oops += 1
                print oops
        # 捕获异常
        except(KeyboardInterrupt, EOFError, ValueError):
            print 'invalid input... try again'


def main():

    while True:
        doprob()
        # 输入了正确结果以后
        try:
            # 是否继续
            opt = raw_input('again?[y] ').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()