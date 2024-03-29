#-*- coding:utf-8 -*-
from ._global import EPSILON
import math

class Vector:

    def __init__(self,lst):
        self._values = list(lst)

    @classmethod
    def zero(cls,dim):
        '''返回一个dim维的零向量'''
        return cls([0] * dim)

    def norm(self):
        '''返回向量的模'''
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        '''返回向量的单位向量'''
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero.")
        return Vector(self._values) / self.norm()

    def __len__(self):
        '''返回向量长度（有多少个元素）'''
        return len(self._values)

    def __add__(self, another):
        '''向量加法，返回结果向量'''
        assert len(self) == len(another),\
            "Error in adding. Length os vectors must be same."
        return Vector([a+b for a,b in zip(self,another)])

    def __sub__(self, another):
        '''向量减法，返回结果向量'''
        assert len(self) == len(another), \
            "Error in adding. Length os vectors must be same."
        return Vector([a - b for a,b in zip(self,another)])

    def dot(self,another):
        '''向量的点乘返回结果标量'''
        assert len(self) == len(another), \
            "Error in adding. Length os vectors must be same."
        return sum(a * b for a, b in zip(self, another))

    def __mul__(self, k):
        '''返回数量乘法的结果向量：self * k'''
        return Vector(k * e for e in self)

    def __rmul__(self,k):
        '''返回数量乘法的结果向量：k * self'''
        return self * k

    def __truediv__(self, k):
        '''返回数量除法的结果向量：self / k'''
        return (1 / k) * self

    def __pos__(self):
        '''返回向量取正的结果向量'''
        return 1 * self

    def __neg__(self):
        '''返回向量取负的结果向量'''
        return -1 * self

    def __iter__(self):
        '''返回向量的迭代器'''
        return self._values.__iter__()

    def __getitem__(self, index):
        '''取出向量的第index元素'''
        return self._values[index]

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "Vector({})".format(",".join(str(e) for e in self._values))