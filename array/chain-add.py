"""
https://www.codewars.com/kata/a-chain-adding-function/train/python
"""
class add:
    def __init__(self, num):
        print('init')
        self.num = num

    def __eq__(self, other):
        print('eq')

        return self.num == other

    def __call__(self, num):
        print('call')
        self.num += num
        return self

    def __add__(self, num):
        print('add')
        self.num += num
        return self

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return self.__str__()
