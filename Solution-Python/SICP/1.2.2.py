#!/usr/bin/env python
# encoding:utf-8

# SICP P26 换零钱问题python实现
# 参考资料 https://blog.csdn.net/renlong0829/article/details/51325201
# 可以用"表格技术"or"记忆技术"（其实就是递归过程中的cache）来进行加速计算

def get_money_value(money_type):
    """获取该零钱种类对应的面值"""
    money_type_set = {
        "1": 1,
        "2": 5,
        "3": 10,
        "4": 25,
        "5": 50
    }
    return money_type_set[str(money_type)]


def count_change(amount):
    """
    递归的核心思路
    n元的兑换方法 = n元的兑换方法（这一次不使用d面值的纸币进行兑换） +
                    n-d元的兑换方法(这次用d面值的纸币进行兑换)

    其实这里通过从从大到小排列面值并赋予一个编号，
    然后根据编号情况表示本次兑换可以使用的纸币范围
    eg：kinds_of_coins = 5            -> 1,2,3,4,5 可用
        kinds_of_coins = 2            -> 1,2 可用 3,4,5种纸币本次选择不用来进行兑换


    递归终止条件
    n < 0 或者没有可用纸币类型进行兑换    ->    0
    n = 0                            ->     1
    """

    def cc(am, kinds_of_coins):
        if am < 0 or kinds_of_coins > 5:
            return 0
        elif am == 0:
            return 1
        else:
            return cc(am - get_money_value(kinds_of_coins), kinds_of_coins) + \
                   cc(am, kinds_of_coins + 1)

    return cc(amount, 1)


if __name__ == '__main__':
    print count_change(100)
