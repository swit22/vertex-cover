# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:13:13 2018

@author: s.witkin
Abstract Min vertex cover setup
"""

from __future__ import division
import pandas as pd
import numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory
opt= SolverFactory('glpk')


model = ConcreteModel()
A = pd.read_csv('Graph2.csv')

model.I = Set(initialize=A.index)
model.J = Set(initialize=A.columns)


model.x = Var(model.J,domain = Boolean, initialize = 1)
  
#A vector of ones
#model.c = Param(A.columns, initialize = {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1})
model.c = Param(model.J, initialize = 1)

#Below returns a constant epression. No good. Not sure how defining sums works in rules/ variables.
#def obj_expression(model):
#    return summation(model.x, model.c, index = model.J) #c'x
#model.OBJ = Objective(rule = obj_expression(model))

model.OBJ = Objective(expr = summation(model.x, model.c, index = model.J))

def ax_constraint_rule(model,i):
    return summation(A.iloc[i,:],model.x) >= 1
model.AxbConstraint = Constraint(model.I, rule = ax_constraint_rule)
print('This has been added to Git")
results = opt.solve(model)
print(model.display())
