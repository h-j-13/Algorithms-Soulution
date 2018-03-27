# -*- coding:utf-8 -*-
import functools


class Solution:
    """斐波那契数列"""
    # 最入门的递归问题

    # 可以用pyhon3的 @functools.lru_cache() 或者 python的默认参数只初始化一次的特性设置个cache

    # python3 - @functools.lru_cache() LRU 装饰器

    # @functools.lru_cache()
    # def Fibonacci(self, n):
    #     if n <= 2:
    #         return 1
    #     else:
    #         return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

    def Fibonacci(self, n, cache={}):
        # cache
        if cache.has_key(str(n)):
            return cache[str(n)]
        else:
            if n == 0:
                cache[str(n)] = 0
            elif n <= 2:
                cache[str(n)] = 1
            else:
                cache[str(n)] = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
            return cache[str(n)]


if __name__ == '__main__':
    print Solution().Fibonacci(10)
    print Solution().Fibonacci(10)
    print Solution().Fibonacci(10)
