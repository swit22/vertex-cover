# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:13:13 2018

@author: s.witkin
Abstract Min vertex cover setup
"""

from __future__ import division
import pandas as pd
from pyomo.environ import *
from pyomo.opt import SolverFactory
opt= SolverFactory('glpk')

model = AbstractModel()
A = pd.read_csv('book2.csv')

model.m = Param(within=NonNegativeIntegers, initialize = len(A))
model.n = Param(within=NonNegativeIntegers, initialize = len(A.columns))
model.I = Set(initialize=A.index)
model.J = Set(initialize=A.columns)
model.a = Param(model.I,model.J, initialize = A)
model.c = Param(model.J, initialize = {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1})

model.x = Var(model.J,domain = Boolean)

def obj_expression(model):
    return summation(model.x, model.c,index = model.J) #c'x

model.OBJ = Objective(rule = obj_expression)
def ax_constraint_rule(model,i):
    return sum(model.a[i,j]*model.x[j] for j in model.J) >= 1
model.AxbConstraint = Constraint(model.I, rule = ax_constraint_rule)


instance = model.create_instance()
results = opt.solve(instance)
instance.display()
