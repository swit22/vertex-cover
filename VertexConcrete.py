# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:13:13 2018

@author: s.witkin
Abstract Min vertex cover setup
"""

from __future__ import division
import pandas as pd
import numpy as np
from pyomo.core import *
from pyomo.environ import *
from pyomo.opt import SolverFactory
opt= SolverFactory('glpk')


model = ConcreteModel()
A = pd.read_csv('book2.csv')

#model.I = Set(initialize=A.index)
#model.J = Set(initialize=A.columns)
#model.x = Var(range(len(A.columns)),domain = Boolean)


model.x = Var(A.columns,domain = Boolean)

#A vector of ones
model.c = Param(A.columns, initialize = {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1})

#initializes them to 1, for some reason it needs initialization
for i in A.columns:
    model.x[i] = 1


def obj_expression(model):
    return summation(model.x, model.c, index = A.columns) #c'x

#model.OBJ = Objective(rule = obj_expression(model))
model.OBJ = Objective(expr = summation(model.x, model.c, index = A.columns))


def ax_constraint_rule(model,i):
    return summation(A.iloc[i,:],model.x) >= 1
model.AxbConstraint = Constraint(range(9), rule = ax_constraint_rule)


results = opt.solve(model)


print(model.display())

