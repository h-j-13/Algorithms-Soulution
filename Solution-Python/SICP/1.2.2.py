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
    n元的兑换方法 = n元的兑换方法（这一次不使用d面值的纸币进行兑换） + n-d元的兑换方法

    递归终止条件
    n < 0 或者没有可用纸币类型进行兑换    ->    0
    n = 0                            ->     1
    """
    def cc(am, kinds_of_coins):
        if am < 0 or kinds_of_coins == 0:
            return 0
        elif am == 0:
            return 1
        else:
            return cc(am - get_money_value(kinds_of_coins), kinds_of_coins) + \
                   cc(am, kinds_of_coins - 1)

    return cc(amount, 5)


if __name__ == '__main__':
    print count_change(100)
