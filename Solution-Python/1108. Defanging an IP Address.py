#!/usr/bin/env python
# encoding:utf-8

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")


# better way
#
# Some may be quick to write a quick replacecall on the string for a one line solution, but it's important to examine
# how this will work. In python, strings are immutable objects, meaning if we are searching for '.', we will have as
# many stack calls underneath the surface when we replace as the number of occurences of '.'in the string.
# Thus, since we cannot modify a string in place like we can an array, and since for a general replacecall we could
# have kinstances of '.', where k<=n, the worst-case time complexity for a replacecall is actually O(n*k)=O(n*n)where
# nis the length of the string.
#
# A better approach would be to merely split the string up into an array each time we see a ., then join these
# elements with the proper '[.]'string. With the splitand joinfunctions, we parse the input twice, once as the
# original string, and once as the split array, however, this equates to a time complexity of O(2*n)=O(n).
#
# Code is below, good luck on your interviews or growing your skills!
#
def defangIPaddr(self, address):
    return ('[.]'.join(address.split('.')))


# https://wiki.python.org/moin/TimeComplexity