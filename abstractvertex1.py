# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:13:13 2018

@author: s.witkin
Abstract Min vertex cover setup
"""

from __future__ import division
from pyomo.environ import *

model = AbstractModel()

model.m = Param(within=NonNegativeIntegers)
model.n = Param(within=NonNegativeIntegers)
model.I = Set()
model.J = Set()
model.a = Param(model.I,model.J)
model.c = Param(model.J, initialize = {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1})

model.x = Var(model.J,domain = Boolean)

def obj_expression(model):
    return summation(model.x, model.c,index = model.J) #c'x

model.OBJ = Objective(rule = obj_expression)
def ax_constraint_rule(model,i):
    return sum(model.a[i,j]*model.x[j] for j in model.J) >= 1
model.AxbConstraint = Constraint(model.I, rule = ax_constraint_rule)


