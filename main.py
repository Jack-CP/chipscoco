
# __author__ = chnegpeng
# __email__ = 1176383558@qq.com
# __date__ = 2020.11.10
# __desc__ = calculate the sum of each figure of a number
a=0


"""
1.题目：给定一个三位数，求每位上的数字之和
2.思考需要哪些变量，先定义变量
"""

sum = 0
number = 123
weight = 100
figure = 0
"""
1.因为不需要遍历一个区间的所有数，所以不用for循环
2.选择 while 循环
3.继续思考谁在while循环中充当变量？
4.陈导给的选择是 weight
"""
while weight >= 1:
    """
    1.因为是各位数上的数字求和，所以要找出对应的数字
    2.利用整除法 可以得到百位，十位，个位数字
    3.利用取余法可以得到剩下的两位数
    """
    figure = number // weight
    number = number % weight
    """
    1。到达上面一步后，思维就卡壳了，我还在想改如何对十位上的数字取整
    2.按照思维惯性，还会继续写 figure = number // weight来求十位，可能会再定义weight等
    3.上面的思路其实忘掉了while作为循环语句的本质了，因为下面的代码只要符合条件就会一直循环执行
    4.再看一下循环条件 weight >= 1.开头已经定义了weight= 100.现在需要重新定义或重新赋值
    """
    weight = weight // 10
    """
    1.一定要熟悉 sum = sum + a 的结构，相当于重新赋值、定义
    2.也就是陈导强调的：在需要的时候就去定义变量
    3.最后一行代码 和 while 形成一个闭环，首尾呼应了
    """
    sum = sum + figure
    print("figure",figure)
    """
    1.还要注意代码缩进，sum写在不同的位置结果就不同，刚刚又弄错了
    """
print("sum",sum)





